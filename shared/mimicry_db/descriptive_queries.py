from mimicry_db.base import session
from mimicry_db.file_path_utils import matched_waveform_summary_filepath
import numpy as np
import pandas as pd

age_at_admission_sql = """
        DATE_PART('year', a.admittime::date) - DATE_PART('year', p.dob::date) """
mean_age_at_admission_sql = "AVG({})".format(age_at_admission_sql)
        

def age_at_admission_by_gender_df(gender):
    sql_query = """
        SELECT 
           p.subject_id,
           p.gender,
           {} as mean_age_at_admission
        FROM 
            patients p
        INNER JOIN 
            admissions a
            ON a.subject_id = p.subject_id
        WHERE 
            p.has_matched_waveform
        AND
            p.gender = '{}'
        GROUP BY
            p.subject_id, p.gender
    """.format(mean_age_at_admission_sql, gender)
    df = pd.read_sql(sql_query, session.bind)
    result_df = drop_duplicates_and_reset_index(df) 
    return result_df

def read_matched_waveform_records():
    return pd.read_csv(matched_waveform_summary_filepath)

def get_unique_patient_and_records_df():
    """ returns a dataframe with 'Patient' and 'Record' as columns """
    result = read_matched_waveform_records()
    result = result[['Patient', 'Record']]
    return drop_duplicates_and_reset_index(result)

def get_unique_subject_id_and_timestamp_df():
    """ converts record info to subject_id and time_stamp """
    patient_record_df = get_unique_patient_and_records_df()

    subject_timestamp_df = pd.DataFrame() 
    subject_timestamp_df['filename'] = patient_record_df.apply(
            lambda x: x.Patient + '-' + x.Record, axis=1)
    subject_timestamp_df['subject_id'] = patient_record_df.apply(
            lambda x: convert_patient_to_subject_id(x.Patient), axis=1)
    subject_timestamp_df['timestamp'] = patient_record_df.apply(
            lambda x: convert_record_to_timestamp(x.Record), axis=1)

    return subject_timestamp_df 

def convert_record_to_timestamp(record):
    date = '-'.join(record.split('-')[0:3])
    time = ':'.join(record.split('-')[3:])
    return ' '.join([date, time])

def convert_patient_to_subject_id(patient):
    return int(patient.split('p')[1])
    
def hadm_id_for_subject_overlapping_time(subject_id, event_time):
    sql_query = """
                SELECT 
                DISTINCT a.hadm_id
                FROM patients p
                INNER JOIN admissions a
                ON p.subject_id = a.subject_id
                WHERE
                    p.subject_id = {}
                AND 
                    (
                    (a.admittime::date, a.dischtime::date) 
                    OVERLAPS 
                    (date '{}', date '{}')
                    )
                """.format(subject_id, event_time, event_time)
    df = pd.read_sql(sql_query, session.bind)
    result = drop_duplicates_and_reset_index(df)
    
    assert len(result.hadm_id.values) < 2 # 1 record can't be for 2 admissions

    if len(result.hadm_id.values) > 0:
        return result.hadm_id.values[0]
    else: 
        return np.nan

def generate_demographic_info_df(limit=None):
    sql_query = """
                 SELECT
                    p.subject_id,
                    p.gender,
                    p.dob,
                    a.deathtime,
                    a.hadm_id,
                    a.admission_type,
                    a.admission_location,
                    a.diagnosis,
                    {} as age_at_admission,
                    icd.icd9_code,
                    icd.seq_num
                 FROM patients p
                 INNER JOIN admissions a
                 ON p.subject_id = a.subject_id
                 INNER JOIN diagnoses_icd icd
                 ON icd.hadm_id = a.hadm_id
                """.format(age_at_admission_sql)
    if limit is not None:
        sql_query += " LIMIT %s" % (limit)
    df = pd.read_sql(sql_query, session.bind)
    result_df = drop_duplicates_and_reset_index(df)
    return result_df

def drop_duplicates_and_reset_index(df):
    df.drop_duplicates(inplace=True)
    df = df.reset_index(drop=True)
    return df
