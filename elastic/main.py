from pyexpat.errors import messages
from connection_elastic import get_es_client

def index_json_to_elastic(index,document):
    es = get_es_client()
    response = es.index(index=index,  document=document)
    return response

