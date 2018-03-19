# Python package for analysis of [MIMIC III database](https://mimic.physionet.org/)

As access to the MIMIC III database is restricted, this python package uses fake data. In order to perform analyses on the real database, start with this [documentation](docs/loading_real_mimic_db.md).

## Instructions for Initialization:
1. Create a Docker container via ```bash container/run.sh```
2. Then, once you are within the docker container: ```source shared/start_session.sh``` 
     * Adds analysis/shared/ to PYTHONPATH
     * Starts postgres
3. Finally, ```source shared/first_time_only.sh```
     * Loads the mimic db into postgres from csv files
     * Adds a column to the patients table (<i>has_matched_waveform</i>) to indicate whether a given patient has an associated waveform.

## Instructions once Docker image has been created:
1. Start the docker container: ```docker start mimicry_db```
2. Attach to the container: ```docker attach mimicry_db```
3. Source the bash script to start the session ```source shared/start_session.sh```

## Example Usage:
Currently, I have written two scripts for initial data exploration and visualization, both within ```shared/scripts/``` - the output for both of these automatically goes to ```shared/scripts/output/```.
* ```s01_get_icd9_categories_for_waveform_records.py```
    * This script creates a pandas df with diagnostic and admission information for all patient admissions that have an associated waveform record.  
    * This is output to a ```.pkl``` file that is then read by ```s02_visualization_of_demographics.py``` (when using the real data, running this script can take several minutes).

* ```s02_visualization_of_demographics.py``` 
    * This script loads the df that was generated in ```s01``` and generates a few helpful visualizations of the data:
<img src="https://github.com/RebeccaClarkson/mimicry-db/blob/master/docs/output/s02_age_and_gender_at_admission.png" align="center" height="200" ></a>
<img src="https://github.com/RebeccaClarkson/mimicry-db/blob/master/docs/output/s02_number_of_icd9_codes_full_df.png" align="center" height="200" ></a>
<img src="https://github.com/RebeccaClarkson/mimicry-db/blob/master/docs/output/s02_disease_category.png" align="center" height="200" ></a>

Copyright 2018, Rebecca L. Clarkson. All rights reserved.
