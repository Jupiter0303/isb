import os

from cryptography.hazmat.primitives.ciphers import algorithms, Cipher, modes
from cryptography.hazmat.primitives import padding


class Symmetric:
    """
    класс для реализации алгоритма симметричного шифрования IDEA
    """

    @staticmethod
    def encrypt(original_data: str, key: bytes) -> bytes:
        """
        шифрование строки данных симметричным ключом
        :param original_data: строка исходных даннных
        :param key: симметричный ключ в байтах
        :return: зашифрованные данные в байтах + величина iv в виде приставки
        """
        iv = os.urandom(8)
        cipher = Cipher(algorithms.IDEA(key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        # паддинг
        padder = padding.ANSIX923(64).padder()
        text = bytes(original_data, 'UTF-8')
        padded_text = padder.update(text) + padder.finalize()
        # шифрование
        c_text = encryptor.update(padded_text) + encryptor.finalize()
        return iv + c_text

    @staticmethod
    def decrypt(encrypt_text: bytes, key) -> bytes:
        """
        дешифрование данных в байтах симметричным ключом
        :param encrypt_text: байты - зашифрованные данные
        :param key: симметричный ключ в байтах
        :return: исходные данные в байтах
        """
        iv = encrypt_text[:8]  # выделяем iv
        cipher = Cipher(algorithms.IDEA(key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        # дешифрование
        dc_text = decryptor.update(encrypt_text[8:]) + decryptor.finalize()
        # убираем паддинги, которые добавили при шифровании
        unpadder = padding.ANSIX923(64).unpadder()
        unpadded_dc_text = unpadder.update(dc_text) + unpadder.finalize()

        return unpadded_dc_text

    @staticmethod
    def generate_key() -> bytes:
        """
        генерация симметричного ключа
        :return: ключ в виде байтов
        """
        return os.urandom(16)
