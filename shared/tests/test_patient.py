from mimicry_db.patient import Patient
from mimicry_db.admission import Admission
from mimicry_db.diagnosis import Diagnosis
import pandas as pd

print("""\n\nTesting Patient\n""")

patient = Patient.get(0)
subject_id = patient.subject_id
admissions_df = pd.read_csv('/analysis/shared/data/mimic_csv_files/ADMISSIONS.csv')
diagnoses_df = pd.read_csv('/analysis/shared/data/mimic_csv_files/DIAGNOSES_ICD.csv')
num_admissions = len(set(admissions_df.HADM_ID[(admissions_df.SUBJECT_ID==subject_id)]))
num_diagnoses = len(set(diagnoses_df.ICD9_CODE[(diagnoses_df.SUBJECT_ID==subject_id)]))

def test_patient():
    assert isinstance(patient, Patient)

def test_patient_admission():
    assert isinstance(patient.admission, list)
    assert len(patient.admission) == num_admissions, len(patient.admission)
    assert isinstance(patient.admission[0], Admission)

def test_patient_diagnosis():
    assert isinstance(patient.diagnosis, list)
    assert len(patient.diagnosis) == num_diagnoses, len(patient.diagnosis)
    assert isinstance(patient.diagnosis[0], Diagnosis)

def test_number_of_admissions():
    assert patient.number_of_admissions() == num_admissions
