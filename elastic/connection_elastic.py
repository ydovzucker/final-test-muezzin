from elasticsearch import Elasticsearch
from dotenv import load_dotenv
import os
from logger import Logger
logger = Logger.get_logger()
load_dotenv()

def get_es_client():
    """
    Returns an Elasticsearch client using host from environment variables.
    """
    try:

        es_host = os.getenv("ES_HOST", "http://localhost:9200")
        logger.info("connection to elastic server was successful")
        return Elasticsearch(es_host)


    except Exception as e:
        logger.error(f"error connecting to elastic server because{e}")