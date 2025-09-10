
import time
from elastic.connection_elastic import get_es_client
from logger_elastic import Logger
logger = Logger.get_logger()
import os
from converter.audio_to_text import AudioToText
class Converter_manager:
    def __init__(self):
        self.converter = AudioToText()
        self.es = get_es_client()
    def insert_txt_to_elastic(self,audio_file_path,document_id): # updates document in elastic to have the translated text from the audio file
        text = self.converter.convert_audio_to_text(audio_file_path)

        # index_name = os.getenv("INDEX_ELASTIC","meta_data_audio")
        index_name = "meta_data_audio"
        document_id = document_id
        new_field_name = "translated_to_text"
        new_field_value = text

        try:
            update_body = {
                "doc": {
                    new_field_name: new_field_value
                }
            }


            # Perform the update operation
            response = self.es.update(index=index_name, id=document_id, body=update_body) # updates the document in elastic with translated text




            # print(response)
            logger.info(response)

            response = self.es.get(index=index_name, id=document_id) # makes sure the document was updated
            if response["found"]:
                document_content = response["_source"]
                print(document_content)
            else:
                print(f"Document with ID '{document_id}' not found in index '{index_name}'.")

            return response
        except Exception as e:
            print(f"An unexpected error occurred updating elasticsearch: {e}")
            logger.error(f"An unexpected error occurred updating elasticsearch: {e}")


