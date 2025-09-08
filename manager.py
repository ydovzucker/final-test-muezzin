import os

from connection_elastic import index_json_to_elastic
from meta_data_files import get_meta_data,convert_meta_data_to_json
from publisher import Publisher
from consumer import consume_meta_data
import json



# def get_all_file_paths(folder_path):
#    """
#    Loops over a folder and its subfolders to get the full path of every file.
#
# #    Args:
# #         folder_path (str): The path to the folder to start the search from.
# #
# #     Returns:
# #         list: A list containing the full paths of all files found.
# #     """
#     all_file_paths = []
#     for root, _, files in os.walk(folder_path):
#         for file in files:
#             full_path = os.path.join(root, file)
#             meta_data = TinyTag.get(full_path)
def run():
    folder_path = 'C:/audio-files'
    for root, _, files in os.walk(folder_path):
        for file in files:
             full_path = os.path.join(root, file)
             tag = get_meta_data(full_path)
             json_meta_data = convert_meta_data_to_json(tag,full_path)
             publisher = Publisher()
             topic = "meta_data_for_audio_file"
             data = json.loads(json_meta_data)

             # headers = {"uniq_id":data["metadata"]["filesize"]}
             # publisher.publish(topic,json_meta_data,headers)
             publisher.publish(topic, json_meta_data)
             consumed_message = consume_meta_data(topic)
             id = consumed_message.headers["uniq_id"]


             index_json_to_elastic()




if __name__ == "__main__":
    run()