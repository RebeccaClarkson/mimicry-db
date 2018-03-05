import pandas as pd
from mimicry_db.base import session
from mimicry_db.patient import Patient

patient = Patient()
assert hasattr(patient, 'has_matched_waveform')

matched_records_df = pd.read_csv('/analysis/shared/scripts/db/waveform_data/MIMIC-III_Matched_Summary_data.csv')
patients = matched_records_df.Patient.values

def process_patient_list(patient_list):   
    removed_p = [s.strip("p") for s in patient_list]
    removed_leading_zeros = [s.lstrip("0") for s in removed_p]
    return [int(patient_id) for patient_id in removed_leading_zeros]

subject_ids_with_waveform = process_patient_list(patients)

all_subject_ids_query = session.query(Patient.subject_id).all()
all_subject_ids = []
for result in all_subject_ids_query:
    all_subject_ids.append(result.subject_id)

# Update each patient that has an associated waveform 
patients = Patient.get_from_subject_ids(subject_ids_with_waveform)
for patient in patients:
    patient.has_matched_waveform = True
    session.commit()
