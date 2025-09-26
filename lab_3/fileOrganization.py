import os

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key

from config import PUBLIC_PEM, PRIVATE_PEM


class FileOrganizer:
    """
    класс для работы с файлами - чтение и запись
    """
    @staticmethod
    def serialization_public_key(public_key) -> None:
        """
        сериализация публичного ключа
        :param public_key:
        :return: None
        """
        try:
            with open(PUBLIC_PEM, 'wb') as public_out:
                public_out.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                                         format=serialization.PublicFormat.SubjectPublicKeyInfo)
                                 )
        except Exception as ex:
            print(f"Ошибка при сериализации публичного ключа: {ex}")

    @staticmethod
    def deserialization_public_key():
        """
        десериализация публичного ключа
        :return: публичный ключ в байтах
        """
        try:
            with open(PUBLIC_PEM, 'rb') as pem_in:
                public_bytes = pem_in.read()
            return load_pem_public_key(public_bytes)
        except Exception as ex:
            print(f"Ошибка при десериализации публичного ключа: {ex}")

    @staticmethod
    def serialization_private_key(private_key) -> None:
        """
        сериализация приватного ключа
        :param private_key:  приватный ключ
        :return: None
        """
        try:
            with open(PRIVATE_PEM, 'wb') as private_out:
                private_out.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                            format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                            encryption_algorithm=serialization.NoEncryption())
                                  )
        except Exception as ex:
            print(f"Ошибка при сериализации приватного ключа: {ex}")

    @staticmethod
    def deserialization_private_key():
        """
           десериализация приватного ключа
           :return: приватный ключ в байтах
        """
        try:
            with open(PRIVATE_PEM, 'rb') as pem_in:
                private_bytes = pem_in.read()
            return load_pem_private_key(private_bytes, password=None, )
        except Exception as ex:
            print(f"Ошибка при десериализации приватного ключа: {ex}")

    @staticmethod
    def save_bytes_to_file(data: bytes, file_path: str) -> None:
        """
        сохранения байтов в файле
        :param data: данные в байтах
        :param file_path: путь к файлу для сохранения
        :return: None
        """
        try:
            with open(file_path, 'wb') as f:
                f.write(data)
        except FileNotFoundError:
            print(f"Файл не найден: {file_path}")
        except Exception as ex:
            print(f"Ошибка при сохранении байтов в файл в функции save_bytes_to_file : {ex}")

    @staticmethod
    def load_bytes_from_file(file_path: str) -> bytes:
        """
        считывание байтов из файла
        :param file_path: путь к файлу
        :return: байты, содержащиеся в файле
        """
        try:
            with open(file_path, 'rb') as f:
                return f.read()
        except FileNotFoundError:
            print(f"Файл не найден: {file_path}")
        except Exception as ex:
            print(f"Ошибка при выводе байтов из файла в функции load_bytes_from_file: {ex}")

    @staticmethod
    def check_file_not_empty(file_path: str) -> bool:
        """
        проверка на наличие данных в файле
        :param file_path: путь к файлу
        :return: bool - результат проверки
        """
        try:
            if os.path.getsize(file_path) == 0:
                print(f"Ошибка! Файл - {file_path} - пустой")
                return False

            return True
        except FileNotFoundError:
            print(f"Файл не найден: {file_path}")
        except Exception as ex:
            print(f"Ошибка при проверке файла в функции check_file_not_empty: {ex}")

    @staticmethod
    def read_txt_file(file_path: str) -> str:
        """
        считывание строки из текстового файла
        :param file_path: путь к файлу
        :return: строка, содержащаяся в нем
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            print(f"Файл не найден: {file_path}")

        except Exception as ex:
            print(f"Ошибка при чтении файла в функции read_txt_file: {ex}")

    @staticmethod
    def write_file_txt(data: str, file_path: str) -> None:
        """
        запись данных в текстовый файл
        :param data: строка для записи
        :param file_path: путь к файлу
        :return: None
        """
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(data)
        except FileNotFoundError:
            print(f"Файл не найден: {file_path}")
        except Exception as ex:
            print(f"Ошибка при записи данных в файл в функции write_file_txt: {ex}")
