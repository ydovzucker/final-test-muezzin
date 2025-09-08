# from kafka import KafkaProducer
# from kafka.errors import NoBrokersAvailable
#
# try:
#     producer = KafkaProducer(bootstrap_servers='localhost:9092')
#     print("Successfully connected to Kafka on localhost:9092 (Producer).")
#     # You can optionally send a test message here
#     # producer.send('test_topic', b'Connection Test Message')
#     # producer.flush()
#     producer.close()
# except NoBrokersAvailable:
#     print("Failed to connect to Kafka. No brokers available at localhost:9092.")
# except Exception as e:
#     print(f"An unexpected error occurred during Kafka connection test: {e}")
from kafka import KafkaConsumer
from kafka.errors import NoBrokersAvailable

try:
    consumer = KafkaConsumer(
        'test_topic',  # A dummy topic name, doesn't need to exist for connection test
        bootstrap_servers='localhost:9092',
        group_id='connection_test_group',
        auto_offset_reset='earliest',
        consumer_timeout_ms=1000  # Set a timeout for polling
    )
    print("Successfully connected to Kafka on localhost:9092 (Consumer).")
    # Attempt to poll for messages (will likely be empty for a connection test)
    # for message in consumer:
    #     print(f"Received message: {message.value.decode('utf-8')}")
    consumer.close()
except NoBrokersAvailable:
    print("Failed to connect to Kafka. No brokers available at localhost:9092.")
except Exception as e:
    print(f"An unexpected error occurred during Kafka connection test: {e}")

