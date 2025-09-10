from elasticsearch.helpers import scan
from classification import Classification
from logger_elastic import Logger
logger = Logger.get_logger()

encrypted_hostile_list = "R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlzcGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2NjdXBhdGlvbixSZWZ1Z2VlcyxJQ0MsQkRT"
encrypted_semi_hostile_list = "RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZSBQYWxlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ=="

def run():
    classification = Classification()

    decoded_hostile_list = classification.decode_encrypted_string(encrypted_hostile_list).split(",")
    decoded__semi_hostile_list = classification.decode_encrypted_string(encrypted_semi_hostile_list).split(",")
    index_name = "meta_data_audio"
    try:
        for doc in scan(classification.es,
                        query={"query": {"match_all": {}}},
                        index=index_name):
            print(f"Document ID: {doc['_id']}, Source: {doc['_source']}")
    #         text = doc['_source']["translated_to_text"]
    #         document_id = doc['_id']
    #         bds_percent = classification.bds_percent(text, decoded_hostile_list,decoded__semi_hostile_list)
    #         is_bds = classification.is_bds(bds_percent)
    #         threat_level = classification.threat_level( bds_percent)
    #         doc = {"bds_percent":bds_percent,"is_bds":is_bds,"threat_level":threat_level}
    #         response = classification.insert_values_into_document( doc, index_name, document_id)
    #         return response
    except Exception as e:
        # Handle other unexpected errors
        logger.error(f"An unexpected error occurred: {e}")
if __name__ == "__main__":
    print(run())

        # 'doc' represents each document found in the index
        # You can access document data using doc['_source']
        # And the document ID using doc['_id']





