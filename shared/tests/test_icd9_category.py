from mimicry_db.icd9_category import get_diagnosis_from_icd9_string, process_icd9_string

code_tests = [
        ('0010', 'infectious'),
        ('0011', 'infectious'),
        ('00320', 'infectious'),
        ('00589', 'infectious'),
        ('0545', 'infectious'),
        ('05444', 'infectious'),
        ('1372', 'infectious'),
        ('1722', 'neoplasms'),
        ('66551', 'pregnancy'),
        ('28989', 'blood'),
        ('2899', 'blood'),
        ('90183', 'injury_poisoning'),
        ('9038', 'injury_poisoning'),
        ('E800', 'physical_accident'),
        ('E812', 'physical_accident'),
        ('V56', 'dialysis_care'),
        ('E870', 'Other: E'),
        ('V40', 'Other: V'),
        ]


def test_icd9_dictionary():
    for code, category in code_tests:
        diagnosis = get_diagnosis_from_icd9_string(code)
        assert diagnosis == category, (code, diagnosis, category)

def test_process_icd_string():
    assert process_icd9_string('V1209') == 'V12.09'
    assert process_icd9_string('V4581') == 'V45.81'
    assert process_icd9_string('V0980') == 'V09.80'
    assert process_icd9_string('V090') == 'V09.0'
    assert process_icd9_string('E9320') == 'E932.0'
