from mimicry_db.admission import Admission
from mimicry_db.diagnosis import Diagnosis
from mimicry_db.diagnosis_description import DiagnosisDescription
from mimicry_db.patient import Patient
import pandas as pd

print("""\n\nTesting Diagnosis\n""")
diagnosis = Diagnosis.get(0)

diagnosis_df = pd.read_csv('/analysis/shared/data/mimic_csv_files/DIAGNOSES_ICD.csv')

def test_summarize_by_icd9_code():
    current_hadm_id_and_patients = (diagnosis_df[(diagnosis_df.ICD9_CODE=='4019')])
    num_admissions = len(set(current_hadm_id_and_patients.HADM_ID))
    num_patients = len(set(current_hadm_id_and_patients.SUBJECT_ID))
    num_patients_calc, num_admissions_calc = Diagnosis.summarize_by_icd9_code('4019')
    assert num_admissions_calc == num_admissions
    assert num_patients_calc == num_patients

def test_diagnosis():
    assert isinstance(diagnosis, Diagnosis)

def test_diagnosis_admission():
    assert isinstance(diagnosis.admission, Admission)

def test_diagnosis_from_admission_for_patient():
    assert isinstance(diagnosis.admission.patient, Patient)

def test_diagnosis_description():
    assert 'scapula' in str(diagnosis.description)
    assert isinstance(diagnosis.description, DiagnosisDescription)
