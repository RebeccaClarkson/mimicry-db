# Python package for analysis of [MIMIC III database](https://mimic.physionet.org/)

As access to the MIMIC III database is restricted, this python package uses fake data. In order to perform analyses on the real database, start with this [documentation](docs/loading_real_mimic_db.md).

## Instructions:
1. Create the Docker container via ```bash container/run.sh```
2. Then, once you are within the docker container: ```bash shared/load_mimic_db.sh``` 
     * Installs mimicry_db as a module (via the setup.py file)
     * Starts postgresql
     * Loads the mimic db into postgres from csv files
     * Adds a column to the patients table (<i>has_matched_waveform</i>) to indicate whether a given patient has an associated waveform.
