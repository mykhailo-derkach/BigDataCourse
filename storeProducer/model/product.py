from faker import Faker
from faker_vehicle import VehicleProvider


class Product(object):

    def __init__(self, name: str, description: str, category: str, barcode: str, price: int):
        self.id = description + '/' + str(price)
        self.name = name
        self.description = description
        self.category = category
        self.barcode = barcode
        self.price = price

    def to_json(self) -> dict:
        return self.__dict__
    
    @staticmethod
    def generate_random_product():
        fake_product = Faker()
        fake_product.add_provider(VehicleProvider)
        return Product(
            name=fake_product.vehicle_make_model(),
            description=fake_product.vehicle_year_make_model_cat(),
            category=fake_product.vehicle_category(),
            barcode=str(fake_product.pyint(min_value=1000000000000, max_value=9999999999999, step=1)),
            price=fake_product.pyint(min_value=20000,   max_value=50000000, step=1000)
            )


