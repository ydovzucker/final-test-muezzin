from pyexpat.errors import messages
from kafka import KafkaConsumer
import json
import time

# from consumer import consume_meta_data
def main():
    # try:
        topic = "meta_data_for_audio_file"
        TOPIC_NAME = topic
        GROUP_ID = None
        print('mmm')
        consumer = KafkaConsumer(
            "meta_data_for_audio_file",  # Replace with your Kafka topic name
            bootstrap_servers='localhost:9092',  # Adjust if your broker is on a different host
            group_id='meta_data_for_files',  # Specify a consumer group ID
            auto_offset_reset='earliest',  # Start reading from the earliest available message
            enable_auto_commit=True,  # Automatically commit offsets
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )
        # print("hi")
        # topic = "meta_data_for_audio_file"
        # consume_meta_data(topic)
    # except Exception as e:
    #     print(e)
    # finally:
    #     print("hello")


        for message in consumer:
            print(f"Received message: {message.value}")
            data = json.loads(message.value)
            id = data["metadata"]["filesize"]
            print(id)
            print("hello")
    # except Exception as e:
    #     print(e)
    # finally:
    #     print("hello")




if __name__ == "__main__":

    main()