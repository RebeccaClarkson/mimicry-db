export PYTHONPATH=/analysis/shared
/etc/init.d/postgresql start
psql -U mimic_user -h localhost -d mimicry_db -f /analysis/shared/scripts/db/buildmimic.sql
psql -U mimic_user -h localhost -d mimicry_db -f /analysis/shared/scripts/db/add_has_matched_waveform.sql
python3 /analysis/shared/scripts/db/alter_db_add_bool_matched_records.py
