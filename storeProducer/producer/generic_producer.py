import json

from confluent_kafka.avro import AvroProducer
from confluent_kafka import avro


class Producer:

    def __init__(self, args):
        self.producer_config = {
            'bootstrap.servers': args.bootstrap_servers,
            'schema.registry.url': args.schema_registry
        }

        self.topic = args.topic

        key_schema = avro.loads('{"type": "string"}')
        value_schema = avro.load(f"./schema/{args.schema_file}")

        self.producer = AvroProducer(
            self.producer_config,
            default_key_schema=key_schema,
            default_value_schema=value_schema
        )

    def send_record(self, key: str, value: json):
        try:
            self.producer.produce(topic=self.topic, key=key, value=value)
        except Exception as e:
            print(f'Exception during producing record for key: {key} in topic: {self.topic}. {e}')
        else:
            print(f'Record with key: {key} in topic: {self.topic} was successfully produced')

    def send_records(self, items: list):
        for item in items:
            self.send_record(key=item.id, value=item.to_json())
        self.producer.flush()
