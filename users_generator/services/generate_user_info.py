from random import randint

from faker import Faker

from users_generator.models import UserInfo

fake = Faker()


def generate_names(amount: int) -> list[str]:
    name_list: list[str] = []
    for name in range(amount):
        name = f"{fake.first_name().lower()}_{str(randint(1970, 2022))}"
        if name in name_list:
            name = f"{'_'.join(fake.first_name().lower())}_{str(randint(1, 1000))}"
        name_list.append(name)
    return name_list


def generate_emails(amount: int) -> list[str]:
    email_list: list[str] = []
    for email in range(amount):
        email = fake.free_email()
        if email in email_list:
            email = f"{fake.first_name().lower()}{randint(1, 1000)}@gmail.com"
        email_list.append(email)
    return email_list


def generate_passwords(amount: int) -> list[str]:
    password_list: list[str] = []
    for password in range(amount):
        password = fake.password(special_chars=False)
        if password in password_list:
            password = fake.password(special_chars=False).reverse()
        password_list.append(password)
    return password_list


def organize_info(amount: int) -> UserInfo:
    names = generate_names(amount=amount)
    emails = generate_emails(amount=amount)
    passwords = generate_passwords(amount=amount)

    for name, email, password in zip(names, emails, passwords):
        yield UserInfo(name=name, email=email, password=password)
