import os
from cryptography.hazmat.primitives.ciphers import algorithms, Cipher, modes
from cryptography.hazmat.primitives import padding



class Symmetric:

    @staticmethod
    def encrypt(original_text: str, key: bytes) -> bytes:
        iv = os.urandom(8)
        cipher = Cipher(algorithms.IDEA(key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        padder = padding.ANSIX923(16).padder()
        text = bytes( original_text, 'UTF-8')
        padded_text = padder.update(text) + padder.finalize()
        c_text = encryptor.update(padded_text) + encryptor.finalize()
        return iv +  c_text

    @staticmethod
    def decrypt(encrypt_text:bytes, key) -> bytes:
        iv = encrypt_text[:8]
        cipher = Cipher(algorithms.IDEA(key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        dc_text = decryptor.update(encrypt_text[8:]) + decryptor.finalize()

        unpadder = padding.ANSIX923(64).unpadder()
        unpadded_dc_text = unpadder.update(dc_text) + unpadder.finalize()

        return unpadded_dc_text

    @staticmethod
    def generate_key() ->bytes:
        return os.urandom(16)
