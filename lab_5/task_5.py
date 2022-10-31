import string
from random import sample


def get_random_password(length: int = 8) -> str:
    # TODO написать функцию генерации случайных паролей
    if not length or length < 0:
        raise ValueError(f'Length value is not correct: {length}')
    allowed_symbols = string.digits + string.ascii_lowercase + string.ascii_uppercase
    return ''.join(sample(allowed_symbols, length))


if __name__ == '__main__':
    print(get_random_password())
    print(get_random_password(4))
    print(get_random_password(10))
    print(get_random_password(16))
    print(get_random_password(0))
    print(get_random_password(-2))
