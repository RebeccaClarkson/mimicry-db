from mimicry_db.diagnosis_description import DiagnosisDescription
from mimicry_db.diagnosis import Diagnosis
from mimicry_db.patient import Patient

print("""\n\nTesting DiagnosisDescription\n""")
description_no_diagnosis = DiagnosisDescription.get()
description_with_diagnosis = DiagnosisDescription.get_by_icd9('81119')

def test_find_by_icd9():
    for diagnosis in DiagnosisDescription.find_by_icd9('V22%'):
        assert diagnosis.icd9_code in ('V220', 'V221', 'V222') 

def test_description_no_diagnosis():
    assert isinstance(description_no_diagnosis, DiagnosisDescription)

def test_find_diagnosed_descriptions():
    diagnosed_descriptions_all = DiagnosisDescription.find_diagnosed_diagnosis_descriptions(
            limit=None)
    assert not description_no_diagnosis.diagnoses
    assert description_no_diagnosis not in diagnosed_descriptions_all
    assert description_with_diagnosis in diagnosed_descriptions_all

    for current_description in diagnosed_descriptions_all[0:10]: 
        assert isinstance(current_description.diagnoses, list)
        assert isinstance(current_description.diagnoses[0], Diagnosis)

def test_diagnoses_for_given_descriptions():
    assert isinstance(description_with_diagnosis.diagnoses, list)
    assert isinstance(description_with_diagnosis.diagnoses[0], Diagnosis)

def test_patients_for_given_descriptions():
    assert isinstance(description_with_diagnosis.patients, list)
    assert isinstance(description_with_diagnosis.patients[0], Patient)

def test_find_by_long_title():
    pregnancy_diagnosis_descriptions = DiagnosisDescription.find_by_long_title('%pregnancy%')
    for diagnosis in pregnancy_diagnosis_descriptions:
        assert 'pregnancy' in diagnosis.long_title
