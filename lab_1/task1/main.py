from constants import KEY_FILE, FILE_DATA, FILE_ENCRYPTION
from encryption import encryption


def read_file(file_path: str) -> str:
    """
    чтение строки из файла
    :param file_path: путь к файлу
    :return: строка данных файла
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {file_path} отсутствует")


def write_to_file(data: str, file_path: str) -> None:
    """
    запись данных в файл
    :param data: строка данных
    :param file_path: путь к файлу
    :return: None
    """
    try:
        with open(f'{file_path}', 'w', encoding='utf-8') as file:
            file.write(data)
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {file_path} отсутствует")


def main():
    """
    чтение из файла ключа
    чтение исходного текста
    запись зашифрованного текста
    :return:None
    """
    try:
        key = read_file(KEY_FILE)
        data = read_file(FILE_DATA)
        write_to_file(encryption(data, key), FILE_ENCRYPTION)
    except Exception as ex:
        print(f" Ошибка: {ex} ")


if __name__ == "__main__":
    main()