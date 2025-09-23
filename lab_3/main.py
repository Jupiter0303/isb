import argparse

from config import INITIAL_FILE, ENCRYPTED_FILE, DECRYPTED_FILE, SYMMETRIC_KEY, PUBLIC_PEM, PRIVATE_PEM
import os
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from symmetric import Symmetric
from asymmetric import Asymmetric
from fileOrganization import (
    serialization_public_key, serialization_private_key,
    deserialization_private_key, save_bytes_to_file,
    load_bytes_from_file, check_file_not_empty,
    read_txt_file,
    write_file_txt
)

def GenerateKeys() -> bool:
    print("Запуск генерации ключей")
    try:
        sym_key = Symmetric.generate_key()
        print("Сгенерирован симметричный ключ")

        private_key, public_ley = Asymmetric.generate_keys()
        print("Сгенерированы асимметричные ключи")

        serialization_public_key(public_ley)
        serialization_private_key(private_key)
        print("Сериализованы публичный и приватный ключи")

        cipher_sym_key = Asymmetric.encrypt_bytes(sym_key, public_ley)
        save_bytes_to_file(cipher_sym_key, SYMMETRIC_KEY)
        print("Зашифрован и сохранен симметричный ключ")

        print("Конец генерации ключей")

    except Exception as ex:
        print(f"Ошибка при генерации ключей: {ex}")
        return False
    return True


def EncryptData() -> bool:
    print("Запуск шифрования данных")
    try:
        if (not (check_file_not_empty(SYMMETRIC_KEY)
                 and check_file_not_empty(PRIVATE_PEM))):
                        print("При шифровании были найдены пустые файлы ключей")
                        return False

        private_key = deserialization_private_key()
        print("Приватный ключ был десериализован")

        original_sym_key = Asymmetric.decrypt(load_bytes_from_file(SYMMETRIC_KEY),
                                              private_key)
        print("Симметричный ключ был извлечен и дешифрован")

        original_data = read_txt_file(INITIAL_FILE)
        print("Исходный текст считан")

        c_data_bytes = Symmetric.encrypt(original_data, original_sym_key)
        print("Исходный текст зашифрован симметричным алгоритмом ")

        save_bytes_to_file(c_data_bytes, ENCRYPTED_FILE)
        print("Исходный текст зашифрован симметричным алгоритмом ")

        print("Конец шифрования данных")

    except Exception as ex:
        print(f"Ошибка при шифровании данных: {ex}")
        return False

    return True


def DecryptData():
    print("Запуск дешифрования данных")
    try:
        if not check_file_not_empty(ENCRYPTED_FILE):
            print("Файл с зашифрованными данными пустой")
            return False

        private_key = deserialization_private_key()
        print("Приватный ключ был десериализован")

        original_sym_key = Asymmetric.decrypt(load_bytes_from_file(SYMMETRIC_KEY),
                                              private_key)
        print("Симметричный ключ был извлечен и дешифрован")

        c_data_bytes =  load_bytes_from_file(ENCRYPTED_FILE)
        original_data_bytes = Symmetric.decrypt(c_data_bytes, original_sym_key)
        original_data = original_data_bytes.decode('utf-8')
        print("Зашифрованный байты были извлечены и конвертированы в текст")

        write_file_txt(original_data, DECRYPTED_FILE)
        print("Данные были записаны в файл с дешифрованным текстом")

        print("Конец дешифрования данных")

    except Exception as ex:
        print(f"Ошибка при дешифровании данных: {ex}")
        return False

    return True

def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-gen', '--generation', help='Запуск режима генерации ключей', action='store_true')
    group.add_argument('-enc', '--encryption', help='Запуск режима шифрования', action='store_true')
    group.add_argument('-dec', '--decryption', help='Запуск режима дешифрования', action='store_true')

    args = parser.parse_args()
    status = False
    if args.generation:
        status = GenerateKeys()
    elif args.encryption :
        status = EncryptData()
    elif args.decryption :
        status = DecryptData()
    else:
        print("Была выбрана неизвестная операция")

    if status:
        print("Операция успешно завершилась")
    else:
        print("Операция завершилась с ошибкой")

    return 0


if __name__ == '__main__':
    main()