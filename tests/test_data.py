from faker import Faker
import random


class TestData:
    """
    Test Data generator
    """



    def __init__(self):
        fake = Faker()
        self.email = fake.email()
        self.gender = "male"
        self.first_name = fake.first_name()
        self.last_name = fake.last_name()
        self.password = fake.password()
        self.birthdate = fake.date()
        self.address = fake.street_address()
        self.city = fake.city()
        self.postal_code = fake.postalcode()
        self.state = fake.state()
        self.phone = fake.numerify("##########")
        self.alias = fake.word()
        self.fphone = "533233455D"
        self.logemail = "test123@o2.pl"
        self.fakpassword = "123432"
        self.goodpassword = "123456"
        self.search_prod = "T-shirt"
        self.cus_ser = "Customer service"
        self.order_no = "123456"
        self.text_message = "uszkodzony rękaw"
    item = "T-shirt"
