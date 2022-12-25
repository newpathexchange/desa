import sys
from pathlib import Path

from confluent_kafka import Consumer
from confluent_kafka.serialization import SerializationContext, MessageField
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroDeserializer

from config import config
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4)

# Read config
if len(sys.argv) > 1:
  cfgsel = sys.argv[1]
else:
  cfgsel = 'default'

cfg = config[cfgsel]()
topic = cfg.FAKE_DATA_TOPIC

schema_registry_client = SchemaRegistryClient({
  'url': cfg.AVRO_SCHEMA_REGISTRY_URL
})

consumer = Consumer({
  'bootstrap.servers': cfg.KAFKA_BOOTSTRAP_SERVERS,
  'security.protocol': cfg.KAFKA_SECURITY_PROTOCOL,
  'sasl.mechanism': cfg.KAFKA_SASL_MECHANISM,
  'sasl.username': cfg.KAFKA_SASL_USERNAME,
  'sasl.password': cfg.KAFKA_SASL_PASSWORD,
  'group.id': cfg.FAKE_DATA_CONSUMER_GROUP,
  'auto.offset.reset': 'earliest',
})

consumer.subscribe([topic])

value_schema_str = schema_registry_client.get_latest_version(f"{topic}-{MessageField.VALUE}").schema.schema_str
value_deserializer = AvroDeserializer(schema_registry_client, value_schema_str)

# Kafka consumer loop
while True:
  avro_msg = consumer.poll(10)

  # Support for Kubernetes probes
  Path('/tmp/alive.txt').touch()

  if avro_msg is None:
    continue

  if avro_msg.error():
    print("Kafka Consumer error: {}".format(msg.error()))
    continue

  event = value_deserializer(avro_msg.value(), SerializationContext(topic, MessageField.VALUE))
  pp.pprint(event)

consumer.close()

