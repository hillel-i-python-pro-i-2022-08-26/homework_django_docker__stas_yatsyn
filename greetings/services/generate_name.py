from faker import Faker

fake = Faker()


# Generate name of user
def generate_name() -> str:
    return fake.first_name()
