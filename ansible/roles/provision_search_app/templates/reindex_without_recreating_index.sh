#!/bin/bash
# Script to reindex all datasets in Elasticsearch without recreating index

if [ "$USER" != "{{ app_user }}" ]; then
    echo "Run this {{ app_user }}"
    exit 1
fi

sudo chown -R {{ app_user }}:etsin {{ search_app_log_base_path }}
source /srv/etsin/pyenv/bin/activate
cd {{ search_app_base_path }}
python reindex.py recreate_index=no
