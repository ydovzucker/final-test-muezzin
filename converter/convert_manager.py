

from elastic.connection_elastic import get_es_client
from logger import Logger
logger = Logger.get_logger()
import os
from audio_to_text import AudioToText
class Converter_manager:
    def __init__(self):
        self.converter = AudioToText()
        self.es = get_es_client()
    def insert_txt_to_elastic(self,audio_file_path,document_id):
        text = self.converter.convert_audio_to_text(audio_file_path)
        index_name = os.getenv("INDEX_ELASTIC","meta_data_audio")
        document_id = document_id
        new_field_name = "translated_to_text"
        new_field_value = text

        try:

            response = self.es.update(
                index=index_name,
                id=document_id,
                body={
                    "doc": {
                        new_field_name: new_field_value
                    }
                }
            )
            print(response)
            logger.info(response)
        except Exception as e:
            logger.error(f"An unexpected error occurred updating elasticsearch: {e}")


    # def manager(self):
    #     folder_path = 'C:/audio-files'
    #     for root, _, files in os.walk(folder_path):
    #         for file in files:
    #             full_path = os.path.join(root, file)
    #             text = self.converter.convert_audio_to_text(full_path)
    #             insert_txt_to_elastic(self,text,document_id)








