from mimicry_db.descriptive_queries import drop_duplicates_and_reset_index
from mimicry_db.descriptive_queries import generate_demographic_info_df
from mimicry_db.descriptive_queries import get_unique_subject_id_and_timestamp_df
from mimicry_db.descriptive_queries import hadm_id_for_subject_overlapping_time
from mimicry_db.file_path_utils import script_output_path
from mimicry_db.icd9_category import get_diagnosis_from_icd9_string
import pandas as pd
import time as time

start_time = time.time()

# Get unique subject_id and timestamps
subject_timestamp_df = get_unique_subject_id_and_timestamp_df()

print("Loaded series in %d seconds" % (time.time() - start_time))

df_list = []
i = 0
start_time = time.time()
demographic_info_df = generate_demographic_info_df() 

print("Loaded demographics in %d seconds" % (time.time() - start_time)) 
print(demographic_info_df.head())

start_time = time.time()
# Get hadm_ids for all admissions that have waveforms
subject_timestamp_df['hadm_id']  = subject_timestamp_df.apply(
        lambda x: hadm_id_for_subject_overlapping_time(x.subject_id, x.timestamp), axis=1)
print("Got hadm_ids in %d seconds" % (time.time() - start_time))
print()    
print(subject_timestamp_df.head())
print(subject_timestamp_df.shape)

print("Now aggregating dfs")

# Create a full df with all this information, by combining the demographic df
# with this aggregated subject_id/timestamp df
for idx, values in subject_timestamp_df.iterrows():

    hadm_id = values['hadm_id']
    subject_id = values['subject_id']
    timestamp = values['timestamp']
    filename = values['filename']

    current_df = demographic_info_df[
            (demographic_info_df.subject_id==subject_id) & 
            (demographic_info_df.hadm_id==hadm_id)]
    current_df['filename'] = filename

    df_list.append(current_df)

    i+=1

print("Aggregated dfs in %d seconds" % (time.time() - start_time))

# Combine all the dfs
df = pd.concat(df_list)
print(df.shape)
# Drop all possible duplicates
df = drop_duplicates_and_reset_index(df)
print(df.shape)
print(df)

df['disease_category'] = pd.Series(df.apply(
        lambda row: get_diagnosis_from_icd9_string(row.icd9_code), axis=1))
df['ones'] = 1

df.to_pickle(script_output_path + 's01_icd9_and_categories_for_waveform_records.pkl')
