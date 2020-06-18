"""Inject test data."""
from json import dumps
from os import getenv
from random import randrange, uniform
from sys import argv

from kafka import KafkaProducer

topic_bwsrv = 'bwserver'
topic_srvubw = 'serverusagebw'


def pub_msg(instance, topic, msg):
    """Publish message to Kafka."""
    try:
        instance.send(topic, msg)
    except Exception as e:
        print(f'Exception during publishing message:\n{e}')
        instance.flush()


def conn_kafka_producer():
    """Provide KafkaProducer instance."""
    _producer = None
    try:
        _producer = KafkaProducer(
            bootstrap_servers=getenv(key='KAFKA_ADDR',
                                     default='localhost:9092'
                                     ),
            value_serializer=lambda v: dumps(v).encode('utf-8')
        )
    except Exception as e:
        print(f'Exception during connecting to Kafka:\n{e}')
    return _producer


if __name__ == '__main__':
    """At start generate test data and do the job."""
    kafka_producer = conn_kafka_producer()
    for i in range(0, int(argv[1])):
        msg_bwsrv = {
            'nblisteners': uniform(a=0.01, b=67108864),
            'bitrate': uniform(a=0.01, b=65536)
        }
        msg_srvubw = {
            'nblisteners': uniform(a=0.01, b=67108864),
            'bitrate': uniform(a=0.01, b=65536),
            'nbdays': randrange(start=1, stop=30),
            'nbhours': randrange(start=1, stop=24)
        }
        pub_msg(kafka_producer, topic_bwsrv, msg_bwsrv)
        pub_msg(kafka_producer, topic_srvubw, msg_srvubw)
    if kafka_producer is not None:
        kafka_producer.close()
