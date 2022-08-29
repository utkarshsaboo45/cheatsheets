from kafka import KafkaConsumer
import json


TOPIC_NAME = "registered_user"
GROUP_ID = "consumer-group-a"


if __name__ == "__main__":
    consumer = KafkaConsumer(
        TOPIC_NAME,
        bootstrap_servers=["192.168.0.103:9092"],
        auto_offset_reset="earliest",
        group_id=GROUP_ID
    )

    print("Starting the Consumer")

    for msg in consumer:
        print(f"Registered User = {json.loads(msg.value)}")