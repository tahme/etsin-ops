#!/bin/sh

nextcloudcmd -u {{ etsin_backup_username }} -p '{{ etsin_backup_password }}' {{ etsin_db_backup_archive_path }} https://kannu.csc.fi/remote.php/webdav/ETSIN_DB_BACKUP
