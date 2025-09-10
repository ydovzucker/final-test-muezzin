# pipeline muezzin


###  this is a special program to detect hostile threats through detecting a folder with  podcast files  and checking them for alarming words and leads to potential threats to national  security to the state of israel and it's people.
the project is done with a pipeline that reads the file paths of this files,gets the meta data for them and sends it to kafka.the consumer then gets the meta data for it and sends it to elasticsearch as a document with a uniq id , then he opens the file and sends the binary object to mongodb with this uniq id , finally he translates the file into text and updates the document in elastic with the translated text.
then the classifier takes the text from the document in elastic and classifies how alarming/dangerous inserts that information in the document with special fields.



##  publisher

---
###  meta_data_files.py 
get_meta_data returns a object with meta data for file

convert_meta_data_to_json takes the object and turns into a dict with all meta data and converts to json

### publisher.py
class Publisher initializes the producer to kafka and send messages with the meta data to kafka

### main.py
main loops through the hole folder and uses the publisher to sent the meta data to kafka

### docker file

### requirements.txt



--------
--------
## elastic

---
### connection_elastic.py
connects to elastic server as a client

### main.py 
index_json_to_elastic sends a json to a index in elastic and creates a document of it 

-----
-----

## mongo

---
### dal_mongo.py
class dalMongo connects to mongo through mongoClient and opens a audio file and send it's binary object to mongo with gridfs

------
------

## converter

____

### audio_to_text.py
class AudioToText uses a library called speech_recognition to convert audio to text 

### convert_manager.py
class Converter_manager converts audio files and inserts the outcome into elastic in the same document as its meta data

------
------


## consumer

_______

### consumer.py
consume_meta_data initializes the consumer to listen to messages of the given topic coming in from the publisher the hole time 

### manager.py 
runs  the flow of the pipeline, runs the consumer to take the messages from kafka with the meta data , sends them to elastic and creates the document for them using the elastic/main , then sends the actual audio as a binary object to mongo as gridfs object using the DalMongo class, then calls for the converter to convert the audio to text and updates the elastic document with the translated_audio field, (didn't see a reason to take it from mongo but wanted it to depend on the consumer so , we make sure elastic has the documents with the meta data before we insert the translated_text field )

------
------

## classifier

______

### classification.py
 Classification is a class that takes a encoded string that contains the hostile words , decodes it and turns in to 2 lists, one of hostile words and one of semi_hostile words, and then he calculates what  is the percent of those words out of all words in the text and if it is really bds and what is the threat level, (the percent is to detect if this if the hostile words in the document are a lot in comparison to the non hostile words witch means they are up to something and not just chatig about it) , that's the logic that configures also if it is bds and what is the threat level , and has also a function to insert this new values into the document in elastic

### main.py 

contains the string of the encoded list of the hostile words 
and loops through the documents in elastic classifing them with the classification class and inserting the new fields into the document


------
------

## docker-compose.yaml 
configuration to run containers[kafka-zookeeper,elastic-kibana,mongo,publisher, consumer] 

## logger_elastic.py

class loger configures that all the logs of the code would be sent to elastic by importing this class everywhere and having a record of the flow weather it was successful or not and there was a error




