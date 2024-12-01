import random


def get_random_email():
    random_number = random.randint(100, 999)
    email = f"ilya.stepanov.16.{random_number}@yandex.ru"
    return email


def get_random_password(valid: bool = True):
    if valid:
        password = random.randint(100000, 999999)
        return password
    else:
        password = random.randint(0, 99999)
        return password

