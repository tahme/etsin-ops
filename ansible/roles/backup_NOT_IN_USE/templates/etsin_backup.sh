#!/bin/sh

TIMESTAMP=$(date +%Y%m%d%H%M%S)
pg_dump --format=custom $ETSIN_DATABASE_NAME -f {{ etsin_db_backup_archive_path }}/etsin_db_{{ deployment_environment_id }}_backup_${TIMESTAMP}.dump
