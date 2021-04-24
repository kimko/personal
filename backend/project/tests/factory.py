from faker import Faker

factory = Faker()
factory.random.seed(42)

name = factory.name()
job = factory.job()
text = factory.text()
phone_number = factory.phone_number()
email = factory.email()
