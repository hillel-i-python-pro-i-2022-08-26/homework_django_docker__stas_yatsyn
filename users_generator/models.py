from typing import NamedTuple


# from django.db import models


# User_layout
class UserInfo(NamedTuple):
    name: str
    password: str
    email: str

    def __str__(self):
        return f"Користувач: {self.name}.\n Email: {self.email}. \nПароль: {self.password}"
