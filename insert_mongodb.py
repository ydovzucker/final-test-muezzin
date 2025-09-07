from pymongo import MongoClient
import gridfs

client = MongoClient('mongodb://localhost:27017/') # Replace with your MongoDB connection string
db = client['audio-to-text'] # Replace with your database name
fs = gridfs.GridFS(db)
def insert_to_mongo(file_path,file_name):


    with open(file_path, 'rb') as f:
        # Upload the file to GridFS
        file_id = fs.put(f, filename=file_name, content_type='audio/wav')
        print(f"File '{file_name}' uploaded with ID: {file_id}")