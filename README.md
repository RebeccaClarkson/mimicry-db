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
