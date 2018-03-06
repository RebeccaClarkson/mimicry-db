from mimicry_db.descriptive_queries import age_at_admission_by_gender_df
from mimicry_db.descriptive_queries import get_unique_patient_and_records_df
from mimicry_db.descriptive_queries import generate_demographic_info_df

print(age_at_admission_by_gender_df('M'))
print(age_at_admission_by_gender_df('F'))

get_unique_patient_and_records_df()
print(generate_demographic_info_df(limit=10))
