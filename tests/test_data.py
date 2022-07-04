from faker import Faker
fake = Faker('pl_PL')

class TestData:
    first_name = fake.first_name()
    last_name = fake.last_name()
    invalid_email = "zlyemail@"
    valid_email = fake.free_email()
    password = "Testowanie2022$"
    sex = "female"