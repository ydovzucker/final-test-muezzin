import os

from meta_data_files import get_meta_data,convert_meta_data_to_json
from publisher.publisher import Publisher
from consumer.consumer import consume_meta_data
from elastic.main import index_json_to_elastic
from dal_mongodb import DalMongo

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
        print(type(message.value))
        print(f"Received message: {message.value}")
        data = json.loads(message.value)
        id =  hash_for_file_name(data["file name"])
        index = "meta_data_audio"
        index_json_to_elastic(index, message.value,id)
        file_path = data["file_path"]
        dal_mongo = DalMongo()
        dal_mongo.insert_to_mongo( file_path, data["file name"], id)






if __name__ == "__main__":
    main()