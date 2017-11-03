#!/bin/bash
# Script to reindex all datasets in Elasticsearch without recreating index

if [ "$USER" != "etsin-user" ]; then
    echo "Run this as etsin-user"
    exit 1
fi

source /srv/etsin/pyenv/bin/activate
cd /srv/etsin/search_index/etsin_search_index
python create_empty_index.py
