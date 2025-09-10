from elastic.main import index_json_to_elastic
from mongo.dal_mongodb import DalMongo

import hashlib
from converter.convert_manager import Converter_manager

import json

from consumer import consume_meta_data
def hash_for_file_name(file_name): # calculates hash for string(for uniq id)

    encoded_string = file_name.encode('utf-8')
    hash_func = hashlib.sha256(encoded_string).hexdigest()[:6]
    return hash_func


def main():
    topic = "meta_data_for_audio_file"
    messages = consume_meta_data(topic) # consumes meta data from kafka for all files
    for message in messages:
        print(f"Received message: {message.value}") # checks that the consumer has succesful the meta data
        data = json.loads(message.value) # converts the json of meta data to dict to extract file name
        id =  hash_for_file_name(data["file name"])
        index = "meta_data_audio"
        index_json_to_elastic(index, message.value,id) # creates a document of the meta data for this file in elasticsearch
        file_path = data["file_path"]
        dal_mongo = DalMongo() # connection to mongo
        dal_mongo.insert_to_mongo( file_path, data["file name"], id) #inserts the binary object of the audio file into mongo db with uniq id
        converter = Converter_manager()

        converter.insert_txt_to_elastic(file_path,id) # updates the document in elastic to have the date itself to translated into text from audio








if __name__ == "__main__":
    main()