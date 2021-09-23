from argparse import ArgumentParser

from generator.user_generator import UserGenerator
from generator.product_generator import ProductGenerator
from producer.generic_producer import Producer


def parse_cli_args():
    arg_parser = ArgumentParser()

    arg_parser.add_argument('--topic', required=True, help='Topic Name')
    arg_parser.add_argument('--bootstrap-servers', required=True, help='Bootstrap Server Address')
    arg_parser.add_argument('--schema-registry', required=True, help='Schema Registry URL')
    arg_parser.add_argument('--schema-file', required=True, help='AVRO schema filename')
    arg_parser.add_argument('--producer', required=True, help='Producer')
    return arg_parser.parse_args()


if __name__ == '__main__':
    args = parse_cli_args()
    print(args)
    producer = Producer(args)

    if args.producer == 'User':
        for users in UserGenerator.generate():
            producer.send_records(users)
    elif args.producer == 'Product':
        for products in ProductGenerator.generate():
            producer.send_records(products)
    else:
        raise ValueError("Producer argument could be only User or Product.")
