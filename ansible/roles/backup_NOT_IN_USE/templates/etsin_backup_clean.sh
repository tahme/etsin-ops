#!/bin/sh

find {{ etsin_db_backup_archive_path }} -type f -mtime +10 -delete
