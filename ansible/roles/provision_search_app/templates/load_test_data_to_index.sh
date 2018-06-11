#!/bin/bash
# Script to reindex all datasets in Elasticsearch without recreating index

if [ "$USER" != "{{ app_user }}" ]; then
    echo "Run this {{ app_user }}"
    exit 1
fi

source {{ python_virtualenv_path }}/bin/activate
cd {{ search_app_base_path }}
python load_test_data.py amount_of_datasets=50
