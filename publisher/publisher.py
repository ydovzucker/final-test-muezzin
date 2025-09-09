import os
from kafka import KafkaProducer,KafkaClient,KafkaConsumer
import json
from dotenv import load_dotenv
from kafka.errors import KafkaError
from logger_elastic import Logger
logger = Logger.get_logger()

load_dotenv()  # Load env vars
class Publisher:
    def __init__(self):
        # Kafka broker(s)
        # brokers = os.getenv("KAFKA_BROKERS","localhost:9092")
        self.producer = KafkaProducer(

            bootstrap_servers='localhost:9092',
            value_serializer=lambda x: json.dumps(x).encode('utf-8'),
            # allow_auto_create_topics=True,
        )





    def publish(self, topic: str, message: dict):
        """
        Publish a single message (dict) to the given Kafka topic
        """
        try:


            b = self.producer.send(topic, value=message)

            self.producer.flush()
            # self.producer.close()# Ensure it is sent immediately
            logger.info(f"Published message to {topic}")

        except KafkaError as e:
            # Handle Kafka-specific errors (e.g., connection issues, invalid topic)
            logger.error(f"KafkaError occurred: {e}")
        except Exception as e:
            # Handle other unexpected errors
            logger.error(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    print("hello")