from random import Random
from time import sleep

from model.product import Product


class ProductGenerator(object):

    @staticmethod
    def generate(amount_of_batches: int = 10, batch_size_from: int = 10, batch_size_to: int = 100) -> list:
        for i in range(amount_of_batches):
            batch_size = Random().randint(a=batch_size_from, b=batch_size_to)
            print(f'Batch #{i} have size {batch_size}')
            products = [Product.generate_random_product() for _ in range(batch_size)]
            yield products
            sleep(3)
