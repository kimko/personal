from faker import Faker

factory = Faker()
factory.random.seed(42)


def generate_payload():
    name = factory.name()
    job = factory.job()
    text = factory.text()
    phone_number = factory.phone_number()
    email = factory.email()
    public_id = factory.text(6)

    return {
        "title": job,
        "short_description": text,
        "name": name,
        "email": email,
        "phone": phone_number,
        "public_id": public_id,
    }
