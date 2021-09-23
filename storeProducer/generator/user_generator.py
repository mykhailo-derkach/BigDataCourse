from random import Random
from time import sleep

from model.user import User

class UserGenerator(object):

    @staticmethod
    def generate(amount_of_batches: int = 10, batch_size_from: int = 10, batch_size_to: int = 100) -> list:
        for i in range(amount_of_batches):
            batch_size = Random().randint(a=batch_size_from, b=batch_size_to)
            print(f'Batch #{i} have size {batch_size}')
            users = [User.generate_random_user() for _ in range(batch_size)]
            yield users
            sleep(3)


