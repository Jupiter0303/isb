from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes


class Asymmetric:
    @staticmethod
    def generate_keys() -> tuple:
        keys = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        return keys, keys.public_key()

    @staticmethod
    def encrypt_str(original_data: str, public_key) -> bytes:
        text = bytes(original_data, 'UTF-8')
        return public_key.encrypt(text,
                                  padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(),
                                               label=None))

    @staticmethod
    def encrypt_bytes(original_bytes: bytes, public_key):
        return public_key.encrypt(original_bytes,
                                  padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(),
                                               label=None))

    @staticmethod
    def decrypt(encrypt_text: bytes, private_key) -> str:
        dc_text = private_key.decrypt(encrypt_text, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                                 algorithm=hashes.SHA256(), label=None))
        return dc_text
