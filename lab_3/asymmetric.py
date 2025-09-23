from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa


class Asymmetric:
    """
    Класс для реализации алгоритма асимметричного шифрования
    """

    @staticmethod
    def generate_keys() -> tuple:
        """
        генерация приватного и публичного ключа
        :return: tuple - кортеж из приватного и публичного ключей
        """
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        return private_key, private_key.public_key()

    @staticmethod
    def encrypt_bytes(original_bytes: bytes, public_key) -> bytes:
        """
        шифрование байтов данных через публичный ключ
        :param original_bytes: исходные данные в байтах
        :param public_key: публичный ключ
        :return: зашифрованные байты
        """
        return public_key.encrypt(original_bytes,
                                  padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                               algorithm=hashes.SHA256(),
                                               label=None
                                               )
                                  )

    @staticmethod
    def decrypt(encrypt_text: bytes, private_key) -> bytes:
        """
               дешифрование байтов данных через приватный ключ
               :param encrypt_text: зашифрованные данные в байтах
               :param private_key: приватный ключ
               :return: расшифрованные байты
               """
        dc_text = private_key.decrypt(encrypt_text,
                                      padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                   algorithm=hashes.SHA256(),
                                                   label=None
                                                   )
                                      )
        return dc_text
