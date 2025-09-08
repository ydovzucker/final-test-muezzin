from elasticsearch import Elasticsearch
import os

def get_es_client():
    """
    Returns an Elasticsearch client using host from environment variables.
    """
    es_host = os.getenv("ES_HOST", "http://localhost:9200")
    return Elasticsearch(es_host)

