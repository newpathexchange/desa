import sys
from time import sleep
from uuid import uuid4
from faker import Faker
from pathlib import Path

from confluent_kafka import Producer
from confluent_kafka.serialization import StringSerializer, SerializationContext, MessageField
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroSerializer

from config import config
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4)
# Fake data generator
fake = Faker()

# Read config
if len(sys.argv) > 1:
  cfgsel = sys.argv[1]
else:
  cfgsel = 'default'

cfg = config[cfgsel]()
topic = cfg.FAKE_DATA_TOPIC

value_schema_str = """
{"namespace": "%s",
 "type": "record",
 "name": "%s",
 "fields": [
    {"name": "name", "type": "string"},
    {"name": "count", "type": ["int", "null"]},
    {"name": "color", "type": ["string", "null"]},
    {"name": "address", "type": ["string", "null"]},
    {"name": "main_text", "type": ["string", "null"]},
    {"name": "mod_text", "type": ["string", "null"]},
    {"name": "notes", "type": ["string", "null"]}
  ]
}
""" % (cfg.AVRO_SCHEMA_NAMESPACE, topic)

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}\n'.format(err))
    else:
        print(f"{msg.partition()}-{msg.offset()} ({sys.getsizeof(msg.value())})")


# Connect to schema registry
print('Connecting to schema registry...')
schema_registry_client = SchemaRegistryClient({
    'url': cfg.AVRO_SCHEMA_REGISTRY_URL
})

# Connect to Kafka
print('Connecting to Kafka...')
producer = Producer({
    'bootstrap.servers': cfg.KAFKA_BOOTSTRAP_SERVERS,
    'security.protocol': cfg.KAFKA_SECURITY_PROTOCOL,
    'sasl.mechanism': cfg.KAFKA_SASL_MECHANISM,
    'sasl.username': cfg.KAFKA_SASL_USERNAME,
    'sasl.password': cfg.KAFKA_SASL_PASSWORD,
    'acks': cfg.KAFKA_PRODUCER_ACKS,
    'compression.type': cfg.KAFKA_PRODUCER_COMPRESSION,
})

string_serializer = StringSerializer('utf_8')
avro_serializer = AvroSerializer(schema_registry_client, value_schema_str)

while True:
    # Support for Kubernetes probes
    Path('/tmp/alive.txt').touch()

    # Generate fake data
    data = {
        "name": fake.name(),
        "count": fake.pyint(),
        "color": fake.color(),
        "address": fake.address(),
        "main_text": fake.text(2048),
        "mod_text": fake.text(750),
        "notes": fake.text(250),
    }

    #pp.pprint(data)

    try:
        producer.produce(
            topic=topic,
            key=string_serializer(str(uuid4()), SerializationContext(topic, MessageField.KEY)),
            value=avro_serializer(data, SerializationContext(topic, MessageField.VALUE)),
            on_delivery=delivery_report
        )
        # handle delivery callbacks
        producer.poll(0)

    except Exception as e:
        print("Message enqueue failed: {}\n{}".format(e,data))

    # Delay configured seconds
    sleep(float(cfg.SLEEP_SECONDS))


