from kafka import KafkaProducer
import json
import time

from data import get_registered_user


TOPIC_NAME = "registered_user"


# To serialize a message (it cannot be an object)
def json_serializer(data):
    return json.dumps(data).encode("utf-8")


# Partitioner method - to decide which partition to send a message to
def get_partition(key, all, available):
    return 1  # Partition ID


producer = KafkaProducer(
    bootstrap_servers=["192.168.0.103:9092"],
    value_serializer=json_serializer,
    # partitioner=get_partition     # When we have multiple partitions and we need to
    #                               # decide which partition to send a message to
)

if __name__ == "__main__":
    # Single Topic, Single Partition, Single Broker
    # or
    # Single Topic, Multiple Partitions, Single Broker
    while True:
        registered_user = get_registered_user()
        print(registered_user)
        producer.send(TOPIC_NAME, registered_user)
        # producer.flush()  ## To tell the producer not to batch messages
                            ## and send them immediately
        time.sleep(5)