from kafka import KafkaConsumer
import json

# from consumer.app.insert_to_mongo import insert_to_mongo


def consume_meta_data(topic):
    TOPIC_NAME = topic
    GROUP_ID = None
    consumer = KafkaConsumer(
        'my_topic',  # Replace with your Kafka topic name
        bootstrap_servers=['localhost:9092'],  # Adjust if your broker is on a different host
        group_id='my_consumer_group',  # Specify a consumer group ID
        auto_offset_reset='earliest',  # Start reading from the earliest available message
        enable_auto_commit=True,  # Automatically commit offsets
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    try:
        for message in consumer:
            print(f"Received message: {message.value}")
            # Process the JSON data (message.value) as needed
    except Exception as e:
        print(f"Error consuming messages: {e}")
    finally:
        consumer.close()
    return consumer
#     arr = []
#     count = 0
#     for message in consumer:
#         arr.append({'message': message.value, 'timestamp': message.timestamp,'topic': message.topic})
#         count += 1
#         if count >= max_massages:
#             break
#     if len(arr) > 0:
#         print('len message:',len(arr) )
#         # insert_to_mongo(TOPIC_NAME,arr)
#     else:
#         print('no new messages')
#     return arr
#
# # print(read_news('raw_tweets_antisemitic',10))
from kafka import KafkaConsumer

consumer = KafkaConsumer('my_topic', bootstrap_servers='localhost:9092')

for message in consumer:
    print(f"Topic: {message.topic}, Partition: {message.partition}, Offset: {message.offset}")
    print(f"Key: {message.key}")
    print(f"Value: {message.value.decode('utf-8')}")

    if message.headers:
        print("Headers:")
        for header_key, header_value in message.headers:
            print(f"  {header_key.decode('utf-8')}: {header_value.decode('utf-8')}")
