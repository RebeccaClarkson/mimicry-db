import numpy as np

all_icd9_categories = {}
all_icd9_categories['numeric'] = [
        ('infectious', [[1, 139]]), 
        ('neoplasms', [[140, 239]]), 
        ('endocrine' , [[240, 279]]), 
        ('blood' , [[280, 289]]),
        ('mental' , [[290, 319]]),
        ('nervous' , [[320, 389]]), 
        ('circulatory' , [[390, 459]]),
        ('respiratory' , [[460, 519]]),
        ('digestive' , [[520, 579]]),
        ('genitourinary' , [[580, 629]]),
        ('pregnancy' , [[630, 679]]),
        ('skin' , [[680, 709]]), 
        ('musculoskeletal', [[710, 739]]),
        ('congenital' , [[740, 759]]),
        ('perinatal' , [[760, 779]]),
        ('ill_defined' , [[780, 799]]),
        ('injury_poisoning' , [[800, 999]])
        ]

all_icd9_categories['circulatory'] = [
        ('Acute Rheumatic Fever', [[390, 392]]),
        ('Chronic rheumatic heart disease', [[393,398]]),
        ('Hypertensive disease', [[401, 405]]),
        ('Ischemic heart disease', [[410, 414]]),
        ('Diseases of pulmonary circulation', [[415, 417]]),
        ('Other forms of heart disease', [[420, 429]]),
        ('Cerebrovascular disease', [[430, 438]]),
        ('Diseases of arteries, arterioles, and capillaries', [[440, 449]]),
        ('Diseases of veins and lymphatics', [[451, 459]])]

all_icd9_categories['endocrine'] = [
        ('Disorders of Thyroid Gland', [[240, 246]]),
        ('Other Endocrine Glands', [[249, 259]]),
        ('Nutritional Deficiencies', [[260, 269]]),
        ('Metabolic and Immunity', [[270, 279]])]


numeric_categories = []
for category, code in all_icd9_categories['numeric']:
    numeric_categories.append(category)

all_icd9_categories['E'] = [
        ('physical_accident', [[800, 807], [810, 848]]),
        ('poisoning', [[850, 869]]), 
        ('fire_accident', [[880, 889]])]

E_categories = []
for category, code in all_icd9_categories['E']:
    E_categories.append(category)

all_icd9_categories['V'] = [
        ('reproductive_care',[[20, 29]]),
        ('infant', [[30, 39]]),
        ('organ_transplant', [[42, 42]]),
        ('dependence_on_machines', [[46, 46]]),
        ('dialysis_care', [[56, 56]])]

V_categories = []
for category, code in all_icd9_categories['V']:
    V_categories.append(category)

def process_icd9_string(icd9_string):   
    if icd9_string.isdigit():
        return "%s.%s" % (icd9_string[0:3], icd9_string[3:])
    elif icd9_string[0] == 'E':
        return "%s.%s" % (icd9_string[0:4], icd9_string[4:])
    elif icd9_string[0] == 'V':
        return "%s.%s" % (icd9_string[0:3], icd9_string[3:])

def get_diagnosis_from_icd9_string(icd9_string):
    icd9_processed_string = process_icd9_string(icd9_string)
    if is_number(icd9_processed_string):
        dict_lookup = 'numeric'
        icd9_numeric = int(np.float(icd9_processed_string))
    else:
        dict_lookup = icd9_processed_string[0]
        icd9_numeric = int(np.float(icd9_processed_string[1:]))

    has_category = False
    for category, code_ranges in all_icd9_categories[dict_lookup]:
        if icd9_in_code_range(icd9_numeric, code_ranges):
            has_category = True
            return category
    
    if not has_category:
        if dict_lookup == 'numeric':
            assert False, "Didn't find icd9_code for numeric value"
        else:
            return "Other: %s" % (dict_lookup)


def icd9_in_code_range(val, code_ranges):
    """ code_ranges is a list of lists """
    return any(val <= code_range[1] and val >= code_range[0] for code_range in code_ranges)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False 

#List of ICD-9 codes 001–139: infectious and parasitic diseases
#List of ICD-9 codes 140–239: neoplasms
#List of ICD-9 codes 240–279: endocrine, nutritional and metabolic diseases, and immunity disorders
#List of ICD-9 codes 280–289: diseases of the blood and blood-forming organs
#List of ICD-9 codes 290–319: mental disorders
#List of ICD-9 codes 320–389: diseases of the nervous system and sense organs
#List of ICD-9 codes 390–459: diseases of the circulatory system
#List of ICD-9 codes 460–519: diseases of the respiratory system
#List of ICD-9 codes 520–579: diseases of the digestive system
#List of ICD-9 codes 580–629: diseases of the genitourinary system
#List of ICD-9 codes 630–679: complications of pregnancy, childbirth, and the puerperium
#List of ICD-9 codes 680–709: diseases of the skin and subcutaneous tissue
#List of ICD-9 codes 710–739: diseases of the musculoskeletal system and connective tissue
#List of ICD-9 codes 740–759: congenital anomalies
#List of ICD-9 codes 760–779: certain conditions originating in the perinatal period
#List of ICD-9 codes 780–799: symptoms, signs, and ill-defined conditions
#List of ICD-9 codes 800–999: injury and poisoning
#List of ICD-9 codes E and V codes: external causes of injury and supplemental classification
