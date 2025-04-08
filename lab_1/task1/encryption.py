from math import ceil
from constants import COLUMNS, UNNECESSARY_CHARACTERS, EMPTY_CHAR


def path_generation(key: str) -> tuple:
    """
    генерирует по ключу кортеж из номеров столбцов на основе строки цифр
    :param key: строка из цифр
    :return: кортеж из номеров столбцов
    """
    if not key.isdigit():
        raise ValueError("Ключ должен содержать только цифры")

    code = []
    used_positions = set()
    n = len(key)
    for start in range(n):
        if start in used_positions:
            continue

        for end in range(start + 1, n + 1):
            num = int(key[start:end])
            if num >= COLUMNS:
                break

            if num not in code:
                code.append(num)
                used_positions.update(range(start, end))
                break
    print(code)
    non_key_columns = set(range(0,COLUMNS)) - (set(code))
    print(non_key_columns)
    non_key_columns = sorted(list(non_key_columns))
    code += non_key_columns
    return tuple(code)


def normalize_text(data: str) -> str:
    """
    подготавливает текст к процессу шифрования
    :param data: исходная строка
    :return: подготовленная строка
    """
    for k in UNNECESSARY_CHARACTERS:
        data = data.replace(k, UNNECESSARY_CHARACTERS[k])

    return data.lower()


def encryption(original_data: str, key: str) -> str:
    """
    шифрование текста методом маршрутной транспозиции
    :param original_data: незашифрованная строка
    :param key: ключ - строка из цифр, по которому шифруем текст
    :return: шифротекст
    """
    data = normalize_text(original_data)
    width = COLUMNS
    height = ceil(len(data) / width)
    data_in_matrix = []
    for x in range(height):
        data_in_matrix.append([])
        for y in range(width):
            index = x * width + y
            if index < len(data):
                data_in_matrix[x].append(data[index])
            else:
                data_in_matrix[x].append(EMPTY_CHAR)

    code = path_generation(key)
    encrypted_data = list()
    print(code)
    for x in range(height):
        for y in code:
            if not data_in_matrix[x][y] == EMPTY_CHAR:
                encrypted_data.append(data_in_matrix[x][y])
    print(len(''.join(encrypted_data)))

    return ''.join(encrypted_data)