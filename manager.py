import os

from meta_data_files import get_meta_data,convert_meta_data_to_json
from publisher.publisher import Publisher
from consumer.consumer import consume_meta_data
from elastic.main import index_json_to_elastic

import hashlib


import json

from consumer.consumer import consume_meta_data
def hash_for_file_name(file_name):

    encoded_string = file_name.encode('utf-8')
    hash_func = hashlib.sha256(encoded_string).hexdigest()[:6]
    return hash_func


def main():
    topic = "meta_data_for_audio_file"
    messages = consume_meta_data(topic)
    for message in messages:
        data = json.loads(message.value)
        id = data["metadata"]["filesize"]
        index_json_to_elastic(id, message)
        file_path = data["file_path"]
        insert_to_mongo( file_path, file_name, id)



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
# def run():
#     try:
#
#         folder_path = 'C:/audio-files'
#         for root, _, files in os.walk(folder_path):
#             for file in files:
#                  full_path = os.path.join(root, file)
#                  tag = get_meta_data(full_path)
#                  json_meta_data = convert_meta_data_to_json(tag,full_path)
#                  publisher = Publisher()
#                  topic = "meta_data_for_audio_file"
#                  data = json.loads(json_meta_data)
#
#                  id = {"uniq_id":data["metadata"]["filesize"]}
#                  # publisher.publish(topic,json_meta_data,headers)
#                  publisher.publish(topic, json_meta_data)
#                  consumed_message = consume_meta_data(topic)
#                  for message in consumed_message:
#                      id = message.value
#     except Exception as e:
#         print(e)
#              # id = consumed_message.headers["uniq_id"]
#
#
#              # index_json_to_elastic(id,consumed_message)




if __name__ == "__main__":
    main()