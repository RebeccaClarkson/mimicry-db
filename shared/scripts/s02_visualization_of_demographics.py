from mimicry_db.descriptive_queries import drop_duplicates_and_reset_index
from mimicry_db.file_path_utils import script_output_path
from mimicry_db.icd9_category import numeric_categories
from mimicry_db.plot_utils import simplify_borders
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

#### Load full df 
full_df = pd.read_pickle(script_output_path + 's01_icd9_and_categories_for_waveform_records.pkl')

# Only include diagnoses that are numeric
full_df = full_df[(full_df.disease_category.isin(numeric_categories))]

# Plot # diagnoses per patient 
df_no_filenames = drop_duplicates_and_reset_index(full_df.drop(['filename'], axis=1))
grouped_by_icd9_code = df_no_filenames['icd9_code'].groupby(df_no_filenames['hadm_id']).count()

plt.figure()
ax = plt.subplot(111)
grouped_by_icd9_code.hist(color='red', align='left')
ax.set_xlabel('number of icd9 codes') 
ax.set_ylabel('count')
simplify_borders(ax)
plt.savefig(script_output_path+ 's02_number_of_icd9_codes_full_df.png', bbox_inches="tight")

# Select for primary diagnosis
def get_primary_diagnoses(df):
    return df[(df.seq_num==1)]

primary_diagnoses_full_df = get_primary_diagnoses(full_df)

def pivot_diagnosis_df(df):
    return df.pivot_table(
        columns = ['disease_category'],
        index = ['subject_id'],
        values = 'ones',
        fill_value=0,
        aggfunc=np.sum
        )

# Get information on disease categories 
primary_diagnoses_df_pivot_full = pivot_diagnosis_df(primary_diagnoses_full_df) 
disease_categories = primary_diagnoses_df_pivot_full.sum().sort_values()

# Isolate male and female patients into separate dataframes
age_and_gender_df = full_df[['hadm_id', 'age_at_admission', 'gender']].drop_duplicates()
males_df = age_and_gender_df[(age_and_gender_df.gender == 'M')]
females_df = age_and_gender_df[(age_and_gender_df.gender == 'F')]

# Plot disease categories for primary diagnosis
plt.figure()
ax = plt.subplot(111)
disease_categories.plot.barh(width=.9, color=sns.xkcd_rgb['light blue'])

ax.set_ylabel('')
ax.set_xlabel('count')
simplify_borders(ax)
plt.tight_layout()
plt.savefig(script_output_path+ 's02_disease_category.png', bbox_inches='tight')

# Plot age and gender

plt.figure()
ax = plt.subplot(111)
bins = list(range(0, 110, 10))
males_df['age_at_admission'].hist(color=sns.xkcd_rgb['light red'], bins=bins)
females_df['age_at_admission'].hist(color=sns.xkcd_rgb['light green'], bins=bins)

ax.legend(['Male', 'Female'], loc='upper left')
ax.set_xlabel('age at admission (years)'); ax.set_ylabel('count')
ax.set_xlim([0, 80])
simplify_borders(ax)
plt.savefig(script_output_path+ 's02_age_and_gender_at_admission.png', bbox_inches='tight')
