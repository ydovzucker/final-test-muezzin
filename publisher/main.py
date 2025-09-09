from publisher import Publisher
from meta_data_files import get_meta_data,convert_meta_data_to_json
import json
import os
from logger_elastic import Logger
logger = Logger.get_logger()
def main():
    try:
        publisher = Publisher()

        folder_path = 'C:/audio-files'
        for root, _, files in os.walk(folder_path):
            for file in files:
                 full_path = os.path.join(root, file)
                 tag = get_meta_data(full_path)
                 json_meta_data = convert_meta_data_to_json(tag,full_path)


                 topic = "meta_data_for_audio_file"
                 data = json.loads(json_meta_data)
                 publisher.publish(topic, json_meta_data)
                 logger.info(f"sent meta data for file{full_path}")
    except Exception as e:
        logger.error(f" error publishing meta data for files to kafka")
if __name__ == "__main__":

    main()