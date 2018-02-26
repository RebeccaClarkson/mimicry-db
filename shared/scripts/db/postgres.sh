/etc/init.d/postgresql start
psql -U pguser -h localhost -d mimicry -f /analysis/shared/scripts/db/buildmimic.sql
