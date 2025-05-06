import math

from constants import BLOCK_SIZE, PI, JAVA_SEQUENCE, CPP_SEQUENCE, RESULT_FILE, CPP_GENERATOR_NAME, JAVA_GENERATOR_NAME
from scipy.special import gammaincc


def FrequencyBitwiseTest(data: list) -> float:
    """
    Частотный побитовый тест
    :param data: бинарная последовательность в списке
    :return: float значение - вероятность возможности генератора производить
             действительно рандомные значения
    """
    sum_sn = 0
    for bit in data:
        sum_sn += 1 if bit == 1 else -1

    sum_sn /= len(data) ** 0.5
    p_value = math.erfc(abs(sum_sn) / (2 ** 0.5))
    return p_value


def IdenticalConsecutiveBitsTest(data: list) -> float:
    """
     Тест на одинаковые подряд идущие биты
    :param data: бинарная последовательность в списке
    :return: float значение - вероятность возможности генератора производить
             действительно рандомные значения
    """
    ones_ratio = sum(data) / len(data)
    if not abs(ones_ratio - 0.5) < (2 / (len(data) ** 0.5)):
        return 0

    alternating_chars_number = 0
    for i in range(0, len(data) - 1):
        if data[i] != data[i + 1]:
             alternating_chars_number += 1

    numerator = abs(alternating_chars_number -
                    2 * len(data) * ones_ratio * (1 - ones_ratio))
    denominator = 2 * ((2 * len(data)) ** 0.5) * ones_ratio * (1 - ones_ratio)
    p_value = math.erfc(numerator / denominator)
    return p_value


def MaxOnesSequenceTest(data: list) -> float:
    """
     Тест на самую длинную последовательность единиц в блоке
    :param data: бинарная последовательность в списке
    :return: float значение - вероятность возможности генератора производить
             действительно рандомные значения
    """
    block_max_ones = [0,0,0,0]
    for block_start in range(0, len(data), BLOCK_SIZE):
        max_ones = 0
        block_end = block_start + BLOCK_SIZE
        i = block_start
        while i < block_end:
            current_number_ones = 0
            while i < block_end  and data[i] == 1:
                current_number_ones += 1
                i += 1

            if current_number_ones > max_ones:
                max_ones = current_number_ones

            i += 1

        if max_ones <= 1:
             block_max_ones[0] += 1

        elif max_ones == 2:
            block_max_ones[1] += 1

        elif max_ones == 3:
            block_max_ones[2] += 1

        else:
            block_max_ones[3] += 1

    chi_squared = 0
    for i in range(len(block_max_ones)):
        chi_squared += ((block_max_ones[i] - 16 * PI[i]) ** 2
                        / (16 * PI[i]))

    p_value = gammaincc(1.5, chi_squared / 2)
    return p_value


def clear_file(file_path: str) -> None:
    """
        чистка файла
        :param file_path: путь к файлу
        :return: None
        """
    try:
        with open(f'{file_path}', 'w'):
            pass
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {file_path} отсутствует")


def write_to_file(randomizer_name: str, data: list, file_path: str) -> None:
    """
    запись результатов в файл
    :param randomizer_name: названия генератора рандомных значений
    :param file_path: путь к файлу
    :param data: бинарная последовательность в списке
    :return: None
    """
    try:
        with open(f'{file_path}', 'a', encoding='utf-8') as file:
            file.write(f" {randomizer_name}: {''.join(map(str, data))}\n "
                       f"FrequencyBitwiseTest: {FrequencyBitwiseTest(data)}\n "
                       f"IdenticalConsecutiveBitsTest: {IdenticalConsecutiveBitsTest(data)}\n "
                       f"MaxOnesSequenceTest: {MaxOnesSequenceTest(data)}\n\n\n ")
    except ValueError:
        raise ValueError("Некорректный аргумент в функции open")
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {file_path} отсутствует")


def main():
    try:
        clear_file(RESULT_FILE)
        write_to_file(JAVA_GENERATOR_NAME, JAVA_SEQUENCE, RESULT_FILE)
        write_to_file(CPP_GENERATOR_NAME, CPP_SEQUENCE, RESULT_FILE)

    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()
