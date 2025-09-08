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
        self.producer = KafkaProducer(
            # bootstrap_servers=brokers.split,
            # bootstrap_servers='localhost:9092',
            # allow_auto_create_topics=True,
            # max_block_ms=120000,
            # value_serializer=lambda v: json.dumps(v).encode("utf-8")
            bootstrap_servers='localhost:9092',
            value_serializer=lambda x: json.dumps(x).encode('utf-8'),
            allow_auto_create_topics=True,
        )
        # self.producer = KafkaProducer(
        #     bootstrap_servers='localhost:9092',
        #     # group_id='meta_data_for_files',
        #     # delivery_timeout_ms=60000,
        #     # max_block_ms=120000,
        #     # value_serializer=lambda x: json.dumps(x).encode('utf-8')
        # )
        # self.headers = [('uniq_id',)
        #     ]
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


            b = self.producer.send(topic, value=message)
            print(b)
            self.producer.flush()
            # self.producer.close()# Ensure it is sent immediately
            print(f"Published message to {topic}")

        except KafkaError as e:
            # Handle Kafka-specific errors (e.g., connection issues, invalid topic)
            print(f"KafkaError occurred: {e}")
        except Exception as e:
            # Handle other unexpected errors
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    p = KafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=lambda x: json.dumps(x).encode('utf-8'),
        allow_auto_create_topics=True,
        # delivery_timeout_ms=60000,
        # acks='all'
    )
    f = p.send("sgaa", {'alk':'blll'})
    p.close()
    print(f.value)