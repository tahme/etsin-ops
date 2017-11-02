import os
from os import path
import json
import yaml


def _get_app_config_from_file():
    with open('/home/etsin-user/app_config') as app_config_file:
        return yaml.load(app_config_file)

def get_elasticsearch_config():
    es_conf = _get_app_config_from_file().get('ELASTICSEARCH', None)
    if not es_conf or not isinstance(es_conf, dict):
        return None

    return es_conf

def get_metax_api_config():
    metax_api_conf = _get_app_config_from_file().get('METAX_API')
    if not metax_api_conf or not isinstance(metax_api_conf, dict):
        return None

    return metax_api_conf

def get_metax_rabbit_mq_config():
    metax_rabbitmq_conf = _get_app_config_from_file().get('METAX_RABBITMQ')
    if not metax_rabbitmq_conf or not isinstance(metax_rabbitmq_conf, dict):
        return None

    return metax_rabbitmq_conf

def write_json_to_file(json_data, filename):
    with open(filename, "w") as output_file:
        json.dump(json_data, output_file)


def write_string_to_file(string, filename):
    with open(filename, "w") as output_file:
        print(f"{string}", file=output_file)


# def load_test_data_into_es(config, delete_index_first=False):
#     from etsin_finder.elasticsearch.elasticsearch_service import ElasticSearchService
#     from etsin_finder.finder import app
#     es_config = get_elasticsearch_config(config)
#     test_data_file_path = path.abspath(os.path.dirname(__file__)) + '/test_data/es_dataset_bulk_request_1.txt'
#
#     app.logger.info("Loading test data into Elasticsearch..")
#     if es_config:
#         es_client = ElasticSearchService(es_config)
#         if es_client:
#             if delete_index_first:
#                 es_client.delete_index()
#
#             if not es_client.index_exists():
#                 if not es_client.create_index_and_mapping():
#                     return False
#
#             with open(test_data_file_path, 'r') as file:
#                 data = file.read()
#             if es_client and data:
#                 if es_client.do_bulk_request(data):
#                     app.logger.info("Test data loaded into Elasticsearch")
#                     return
#
#     app.logger.error("Loading test data into Elasticsearch failed")
