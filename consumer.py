from kafka import KafkaConsumer
import json
import common

consumer = KafkaConsumer(common.topic_name, 
                         auto_offset_reset='earliest',
                         bootstrap_servers=[common.broker_1], 
                         api_version=(0, 10), 
                         value_deserializer = json.loads,
                         consumer_timeout_ms=1000)
