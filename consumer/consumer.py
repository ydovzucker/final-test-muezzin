from asyncio import timeout

from kafka import KafkaConsumer
import json

# from consumer.app.insert_to_mongo import insert_to_mongo


def consume_meta_data(topic):
    TOPIC_NAME = topic
    GROUP_ID = None
    print('mmm')
    consumer = KafkaConsumer(
        topic,  # Replace with your Kafka topic name
        bootstrap_servers='localhost:9092',  # Adjust if your broker is on a different host
        group_id='meta_data_for_files',  # Specify a consumer group ID
        auto_offset_reset='earliest',  # Start reading from the earliest available message
        enable_auto_commit=True,
        consumer_timeout_ms=100000,# Automatically commit offsets
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),


    )
    # print(consumer)

    # try:
    #     for message in consumer:
    #
    #
    #         print(f"Received message: {message.value}")
    #         # Process the JSON data (message.value) as needed
    #
    # except Exception as e:
    #     print(f"Error consuming messages: {e}")
    # finally:
    #
    #     consumer.close()
    return consumer

if __name__ == "__main__":
    topic = "meta_data_for_audio_file"
    consume_meta_data(topic)