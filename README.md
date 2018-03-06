# Python package for analysis of [MIMIC III database](https://mimic.physionet.org/)

As access to the MIMIC III database is restricted, this python package uses fake data. In order to perform analyses on the real database, start with this [documentation](docs/loading_real_mimic_db.md).

## Instructions:
1. Start a Docker container via ```bash container/run.sh```
2. Load the mimic db (or my constructed data): ```bash shared/load_mimic_db.sh```
