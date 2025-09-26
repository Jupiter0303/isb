import argparse

from asymmetric import Asymmetric
from config import (
    DECRYPTED_FILE,
    ENCRYPTED_FILE,
    INITIAL_FILE,
    PRIVATE_PEM,
    SYMMETRIC_KEY
)
from fileOrganization import FileOrganizer
from symmetric import Symmetric


def generate_keys() -> bool:
    """
        Сюжет генерации ключей гибридной системы и шифрования симметричного ключа
        :arg: None
        :return: bool - корректность выполнения
        """
    print("Запуск генерации ключей")
    try:
        sym_key = Symmetric.generate_key()
        print("Сгенерирован симметричный ключ")

        private_key, public_ley = Asymmetric.generate_keys()
        print("Сгенерированы асимметричные ключи")

        FileOrganizer.serialization_public_key(public_ley)
        FileOrganizer.serialization_private_key(private_key)
        print("Сериализованы публичный и приватный ключи")

        cipher_sym_key = Asymmetric.encrypt_bytes(sym_key, public_ley)
        FileOrganizer.save_bytes_to_file(cipher_sym_key, SYMMETRIC_KEY)
        print("Зашифрован и сохранен симметричный ключ")

        print("Конец генерации ключей")

    except Exception as ex:
        print(f"Ошибка при генерации ключей: {ex}")
        return False
    return True


def encrypt_data() -> bool:
    """
    Сюжет шифрования данных симметричным шифрованием
    :return: bool - корректность выполнения
    """
    print("Запуск шифрования данных")
    try:
        if not (FileOrganizer.check_file_not_empty(SYMMETRIC_KEY)
                and FileOrganizer.check_file_not_empty(PRIVATE_PEM)):
            print("При шифровании были найдены пустые файлы ключей")
            return False

        private_key = FileOrganizer.deserialization_private_key()
        print("Приватный ключ был десериализован")

        original_sym_key = Asymmetric.decrypt(
            FileOrganizer.load_bytes_from_file(SYMMETRIC_KEY),
            private_key
        )
        print("Симметричный ключ был извлечен и дешифрован")

        original_data = FileOrganizer.read_txt_file(INITIAL_FILE)
        print("Исходный текст считан")

        c_data_bytes = Symmetric.encrypt(original_data, original_sym_key)
        print("Исходный текст зашифрован симметричным алгоритмом ")

        FileOrganizer.save_bytes_to_file(c_data_bytes, ENCRYPTED_FILE)
        print("Исходный текст зашифрован симметричным алгоритмом ")

        print("Конец шифрования данных")

    except Exception as ex:
        print(f"Ошибка при шифровании данных: {ex}")
        return False

    return True


def decrypt_data():
    """
        Сюжет дешифрования шифротекста
        :return: bool - корректность выполнения
        """
    print("Запуск дешифрования данных")
    try:
        if not FileOrganizer.check_file_not_empty(ENCRYPTED_FILE):
            print("Файл с зашифрованными данными пустой")
            return False

        private_key = FileOrganizer.deserialization_private_key()
        print("Приватный ключ был десериализован")

        original_sym_key = Asymmetric.decrypt(
            FileOrganizer.load_bytes_from_file(SYMMETRIC_KEY),
            private_key
        )
        print("Симметричный ключ был извлечен и дешифрован")

        c_data_bytes = FileOrganizer.load_bytes_from_file(ENCRYPTED_FILE)
        original_data_bytes = Symmetric.decrypt(c_data_bytes, original_sym_key)
        original_data = original_data_bytes.decode('utf-8')
        print("Зашифрованный байты были извлечены и конвертированы в текст")

        FileOrganizer.write_file_txt(original_data, DECRYPTED_FILE)
        print("Данные были записаны в файл с дешифрованным текстом")

        print("Конец дешифрования данных")

    except Exception as ex:
        print(f"Ошибка при дешифровании данных: {ex}")
        return False

    return True


def main():
    """
        Главная функция программы. Реализует парсинг аргументов командной строки,
         на основе которых запускает тот или иной сюжет гибридного шифрования
        :return:
        """
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-gen', '--generation', help='Запуск режима генерации ключей', action='store_true')
    group.add_argument('-enc', '--encryption', help='Запуск режима шифрования', action='store_true')
    group.add_argument('-dec', '--decryption', help='Запуск режима дешифрования', action='store_true')

    args = parser.parse_args()
    status = False
    if args.generation:
        status = generate_keys()
    elif args.encryption:
        status = encrypt_data()
    elif args.decryption:
        status = decrypt_data()
    else:
        print("Была выбрана неизвестная операция")

    if status:
        print("Операция успешно завершилась")
    else:
        print("Операция завершилась с ошибкой")

    return 0


if __name__ == '__main__':
    main()
