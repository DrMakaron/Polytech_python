# TODO решить с помощью list comprehension и распечатать его

from pprint import pprint


def convert_digits(digits: list[int]) -> list[dict]:
    methods = {'bin': bin, 'oct': oct, 'hex': hex}
    return [{method_type: method(digit) for method_type, method in methods.items()} | {'dec': digit} for digit in digits]


if __name__ == '__main__':
    result = convert_digits(list(range(16)))
    pprint(result)
