import os
from kafka import KafkaProducer,KafkaClient,KafkaConsumer
import json
from dotenv import load_dotenv
from kafka.errors import KafkaError

load_dotenv()  # Load env vars
class Publisher:
    def __init__(self):
        # Kafka broker(s)
        # brokers = os.getenv("KAFKA_BROKERS","localhost:9092")
        # self.producer = KafkaProducer(
        #     bootstrap_servers=brokers.split,
        #     allow_auto_create_topics=True,
        #     max_block_ms=120000,
        # value_serializer=lambda v: json.dumps(v, default=str).encode("utf-8")
        #
        # )
        self.producer = KafkaProducer(
            bootstrap_servers=['localhost:9092'],
            allow_auto_create_topics=True,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')

        )
        # brokers = os.getenv("KAFKA_BROKERS")
        # self.producer = KafkaProducer(
        #     bootstrap_servers=brokers.split(","),
        #
        #     value_serializer=lambda v: json.dumps(v, default=str).encode("utf-8")

        # )

    def publish(self, topic: str, message: dict):
        """
        Publish a single message (dict) to the given Kafka topic
        """
        try:

            self.producer.send(topic, value=message)
            self.producer.flush()  # Ensure it is sent immediately
            print(f"Published message to {topic}")

        except KafkaError as e:
            # Handle Kafka-specific errors (e.g., connection issues, invalid topic)
            print(f"KafkaError occurred: {e}")
        except Exception as e:
            # Handle other unexpected errors
            print(f"An unexpected error occurred: {e}")

