from mimicry_db.admission import Admission
from mimicry_db.patient import Patient
from mimicry_db.diagnosis import Diagnosis

print("""\n\nTesting Admission\n""")

admission1 = Admission.get(0)
admission13 = Admission.get(12)

def test_admission1():
    assert isinstance(admission1, Admission)

def test_admission1_patient():
    assert isinstance(admission1.patient, Patient)

def test_admission1_diagnoses():
    assert isinstance(admission1.diagnoses, list)
    assert len(admission1.diagnoses) == 5, len(admission1.diagnoses)
    assert len(admission13.diagnoses) == 4, len(admission13.diagnoses)
    assert isinstance(admission1.diagnoses[0], Diagnosis)

def test_number_of_diagnoses():
    assert admission1.number_of_diagnoses() == 5
