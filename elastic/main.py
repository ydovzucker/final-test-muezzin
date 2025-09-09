from pyexpat.errors import messages
from elastic.connection_elastic import get_es_client

def index_json_to_elastic(index,document,document_id):
    es = get_es_client()
    index_name = index

    # Create index with default settings (Elasticsearch will infer mappings on first document)
    if not es.indices.exists(index=index_name):
        es.indices.create(index=index_name)
        print(f"Index '{index_name}' created.")
    else:
        print(f"Index '{index_name}' already exists.")
    try:
        response = es.index(index=index_name, id=document_id, body=document)
        print(response)
        response_1 = es.get(index=index_name, id=document_id)
        if response_1['found']:
            print(f"Document with ID '{document_id}' found in index '{index_name}'.")
            print(response_1['_source'])  # Print the source data of the document
        else:
            print(f"Document with ID '{document_id}' not found in index '{index_name}'.")
    except Exception as e:
        print(f"Error retrieving document: {e}")
    # response = es.index(index=index,  document=document)
    # return response

