from elasticsearch import Elasticsearch
import os

def get_es_client():
    """
    Returns an Elasticsearch client using host from environment variables.
    """
    es_host = os.getenv("ES_HOST", "http://localhost:9200")
    return Elasticsearch(es_host)
# mapping = {
#     "mappings": {
#         "properties": {
#             "TweetID": {"type": "keyword"},          # keep as string for uniqueness
#             "text": {"type": "text"},
#             "Antisemitic": {"type": "boolean"},      # store as boolean (0/1)
#             "CreateDate": {"type": "date"},          # use default ISO format, no custom format
#             "sentiment": {"type": "keyword"},
#             "weapons": {"type": "keyword"}
#         }
#     }
# }
def index_json_to_elastic(index,id,document):
    es = get_es_client()
    response = es.index(index=index, id=id, document=document)