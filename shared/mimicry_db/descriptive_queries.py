from mimicry_db.base import session
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
            p.gender = '{}'
        GROUP BY
            p.subject_id, p.gender
    """.format(mean_age_at_admission_sql, gender)
    df = pd.read_sql(sql_query, session.bind)
    result_df = drop_duplicates_and_reset_index(df) 
    return result_df

def drop_duplicates_and_reset_index(df):
    df.drop_duplicates(inplace=True)
    df = df.reset_index(drop=True)
    return df
