Fake data is within these folders of the module:
```
├── data
│   ├── mimic_csv_files
│   │   ├── ADMISSIONS.csv
│   │   ├── DIAGNOSES_ICD.csv
│   │   ├── D_ICD_DIAGNOSES.csv
│   │   ├── PATIENTS.csv
│   └── waveform_data
│       ├── MIMIC-III_Matched_Summary_data.csv
```

* Overwrite <i> ADMISSIONS.csv, DIAGNOSES_ICD.csv, D_ICD_DIAGNOSES.csv, </i> and <i> PATIENTS.csv </i> with data from the real MIMIC db. 


* You will also need to create a csv file called MIMIC-III_Matched_Summary_data.csv based on [MIMIC-III Waveform Database Matched Subset](https://physionet.org/physiobank/database/mimic3wdb/matched/), which has the following structure:

| patient          | record                 | file       |
|:-----------------|:-----------------------|-----------:|
| p000001          | 1943-03-16-16-05       | 1          |
