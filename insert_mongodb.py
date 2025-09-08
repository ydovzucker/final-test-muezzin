from pymongo import MongoClient
import gridfs


class Fetcher:
    def __init__(self):
        self.uri = "mongodb+srv://IRGC:iraniraniran@iranmaldb.gurutam.mongodb.net"
        self.client = MongoClient(self.uri)
        self.db = self.client['audio-to-text']
        self.col = self.db["tweets"]
        self.fs = gridfs.GridFS(self.db)

# client = MongoClient('mongodb://localhost:27017/') # Replace with your MongoDB connection string

    def insert_to_mongo(self,file_path,file_name):


        with open(file_path, 'rb') as f:
            # Upload the file to GridFS
            file_id = self.fs.put(f, filename=file_name, content_type='audio/wav')
            print(f"File '{file_name}' uploaded with ID: {file_id}")