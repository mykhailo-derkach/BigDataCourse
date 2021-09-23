from faker import Faker


class User(object):

    def __init__(self, first_name: str, last_name: str, age: int, email: str, address: str,
                 gender: str, job: str, has_children_under_16: bool):
        self.id = email
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address
        self.gender = gender
        self.job = job
        self.has_children_under_16 = has_children_under_16

    def to_json(self) -> dict:
        return self.__dict__
    
    @staticmethod
    def generate_random_user():
        fake_user = Faker()
        fake_gender = fake_user.random_element(elements=('M', 'F'))
        fake_first_name = fake_user.first_name_male() if fake_gender == 'M' else fake_user.first_name_female()
        fake_last_name = fake_user.last_name_male() if fake_gender == 'M' else fake_user.last_name_female()
        fake_age = fake_user.pyint(min_value=10, max_value=99, step=1)
        fake_has_children_under_16 = fake_user.pybool() if 18 < fake_age < 50 else False
        return User(

            first_name=fake_first_name,
            last_name=fake_last_name,
            age=fake_age,
            email=fake_user.email(),
            address=fake_user.address(),
            gender=fake_gender,
            job=fake_user.job(),
            has_children_under_16=fake_has_children_under_16
            )


