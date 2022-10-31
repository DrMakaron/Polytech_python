from collections import Counter


def get_count_char(str_: str) -> dict:
    buffer = []

    for char in str_.lower().strip().replace(' ', ''):
        if char.isalpha():
            buffer.append(char)

    result = dict(Counter(''.join(buffer)))
    return result


if __name__ == '__main__':

    main_str = """
        Данное предложение будет разбиваться на отдельные слова. 
        В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
        Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
    """
    print(get_count_char(main_str))
