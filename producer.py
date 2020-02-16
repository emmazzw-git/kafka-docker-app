from kafka import KafkaProducer
import json
import uuid

server = 'broker:9092'
topic_name = "payments-stream"
message = json.dumps({"name": "Mark"})

def publish_message(producer_instance, topic_name, key, value):
    try:
        key_bytes = bytes(key, encoding='utf-8')
        value_bytes = bytes(value, encoding='utf-8')
        producer_instance.send(topic_name, key=key_bytes, value=value_bytes)
        producer_instance.flush()
        print('Message published successfully.')
    except Exception as ex:
        print('Exception in publishing message')
        print(str(ex))


def connect_kafka_producer(server):
    _producer = None
    try:
        _producer = KafkaProducer(bootstrap_servers=[server], api_version=(0, 10))
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    finally:
        return _producer



if __name__ == '__main__':
    server = 'broker:9092'
    topic_name = "payments-stream"
    message = json.dumps({"name": "Mark"})
    kafka_producer = connect_kafka_producer(server)
    publish_message(kafka_producer, topic_name, str(uuid.uuid4()), message)




