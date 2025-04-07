from decryption import create_key, decoding
from constants import ENCRYPTED_DATA_PATH, DECRYPTED_DATA_PATH, KEY_PATH


def read_file(file_path: str) -> str:
    """
    чтение строки из файла
    :param file_path: путь к файлу
    :return: строка данных файла
    """
    try:
        with open(f'{file_path}', 'r', encoding='utf-8') as file:
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
    Берем из файла шифротекст в виде строки.
    Формируем ключ через create_key и заносим в файл для него.
    Дешифрируем исходник и результат заносим в файл для него.
    :return:
    """
    try:
        encrypted_data = read_file(ENCRYPTED_DATA_PATH)

        key = create_key(encrypted_data)

        write_to_file(decoding(encrypted_data,key), DECRYPTED_DATA_PATH)

        write_to_file(str(key), KEY_PATH)

    except Exception as ex:
        print(f" Ошибка: {ex} ")


if __name__ == "__main__":
    main()
