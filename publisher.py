import json
import uuid
import common
from producer import publish_message, connect_kafka_producer
from consumer import consumer

def main():
    message = json.dumps({"name": "Emma"})
    kafka_producer = connect_kafka_producer(common.broker_1)
    publish_message(kafka_producer, common.topic_name, str(uuid.uuid4()), message)
    for msg in consumer:
        print(msg.key.decode("utf-8"), msg.value)

if __name__ == '__main__':
    main()
