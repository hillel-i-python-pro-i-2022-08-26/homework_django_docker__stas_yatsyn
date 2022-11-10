from random import randint, choice
from typing import Iterator

from faker import Faker

from phone_book.models import Contact
from phone_book.services.type_variables import PHONE_NUMBER, BIRTHDAY

fake = Faker()


def generate_phone_number() -> PHONE_NUMBER:
    suffix = ["63", "50", "67", "97", "98", "73", "68", "66"]
    prefix = randint(1000000, 9999999)
    return f"0{choice(suffix)}{prefix}"


def generate_contact_birthday() -> BIRTHDAY:
    year = randint(1960, 2005)
    month = randint(1, 12)
    day = randint(1, 28)
    return f"{year}-{month}-{day}"


def organize_info(amount: int = 10) -> Iterator[Contact]:
    for _ in range(amount):
        yield Contact(
            name=fake.first_name(),
            phone=generate_phone_number(),
            birthday_date=generate_contact_birthday(),
        )
