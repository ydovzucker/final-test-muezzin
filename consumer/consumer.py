import os
from asyncio import timeout

from kafka import KafkaConsumer
import json

# from consumer.app.insert_to_mongo import insert_to_mongo


def consume_meta_data(topic):

    print('mmm')
    consumer = KafkaConsumer( # initializes the consumer
        topic,
        bootstrap_servers=os.getenv("BOOTSTRAP_SERVERS",'localhost:9092'), # Adjust if your broker is on a different host
        group_id='meta_data_for_files',  # Specify a consumer group ID
        auto_offset_reset='earliest',  # Start reading from the earliest available message
        enable_auto_commit=True,
        consumer_timeout_ms=100000,# Automatically commit offsets
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),

    )

    return consumer

if __name__ == "__main__":
    topic = "meta_data_for_audio_file"
    consume_meta_data(topic)