from random import randint


def get_unique_list_numbers() -> list[int]:
    # TODO написать функцию для получения списка уникальных целых чисел
    buffer = []
    while len(buffer) < 15:
        a = randint(-10, 10)
        if a not in buffer:
            buffer.append(a)

    return buffer


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
