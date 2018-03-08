from mimicry_db.descriptive_queries import age_at_admission_by_gender_df
from mimicry_db.descriptive_queries import hadm_id_for_subject_overlapping_time
from mimicry_db.descriptive_queries import generate_demographic_info_df
from mimicry_db.descriptive_queries import read_matched_waveform_records
from mimicry_db.descriptive_queries import get_unique_patient_and_records_df
from mimicry_db.descriptive_queries import convert_record_to_timestamp
from mimicry_db.descriptive_queries import convert_patient_to_subject_id
from mimicry_db.descriptive_queries import get_unique_subject_id_and_timestamp_df
import pandas as pd
import numpy as np


def test_age_at_admission_by_gender_df():
    df = age_at_admission_by_gender_df('M')
    assert isinstance(df, pd.DataFrame)
    assert df['gender'].unique() == 'M'

def test_read_matched_waveforms():
    result = read_matched_waveform_records()
    assert 'Patient' in result.columns
    assert 'Record' in result.columns

def test_get_unique_patient_and_records_df():
    result = get_unique_patient_and_records_df()
    assert 'Patient' in result.columns
    assert 'Record' in result.columns
    assert result['Patient'][0] == 'p000001'
    assert isinstance(result, pd.DataFrame)
    assert isinstance(result.values[0], np.ndarray)

def test_get_unique_subject_id_and_timestamp_df():
    result = get_unique_subject_id_and_timestamp_df()
    assert isinstance(result, pd.DataFrame)
    assert 'filename' in result.columns
    assert 'subject_id' in result.columns
    
def test_convert_record_to_timestamp():
    timestamp = convert_record_to_timestamp('2144-02-06-15-02')
    assert timestamp == '2144-02-06 15:02', timestamp

def test_convert_patient_to_subject_id():
    subject_id = convert_patient_to_subject_id('p000020')
    assert subject_id == 20
    subject_id = convert_patient_to_subject_id('p000001')
    assert subject_id == 1

def test_hadm_id_for_subject_overlapping_time():
    subject_id = 1
    event_time = '2043-03-16 16:05'
    hadm_id = hadm_id_for_subject_overlapping_time(subject_id, event_time)
    assert hadm_id == 1

def test_generate_demographic_info_df():
    result = generate_demographic_info_df()
    assert isinstance(result, pd.DataFrame)
    assert 'subject_id' in result.columns
    assert len(result) == 53
    assert len(set(result.gender)) == 2
    assert len(set(result.hadm_id)) == 13
