from config import PUBLIC_PEM, PRIVATE_PEM
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key


def serialization_public_key(public_key)->None:
    with open(PUBLIC_PEM, 'wb') as public_out:
        public_out.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
             format=serialization.PublicFormat.SubjectPublicKeyInfo))

def deserialization_public_key():
    with open(PUBLIC_PEM, 'rb') as pem_in:
        public_bytes = pem_in.read()
    return load_pem_public_key(public_bytes)


def serialization_private_key(private_key)->None:
    with open(PRIVATE_PEM, 'wb') as private_out:
        private_out.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
              format=serialization.PrivateFormat.TraditionalOpenSSL,
              encryption_algorithm=serialization.NoEncryption()))


def deserialization_private_key():
    with open(PRIVATE_PEM, 'rb') as pem_in:
        private_bytes = pem_in.read()
    return load_pem_private_key(private_bytes, password=None, )



def save_bytes_to_file(data: bytes, file_path: str) -> None:
    with open(file_path, 'wb') as f:
        f.write(data)


def load_bytes_from_file(file_path: str) -> bytes:
    with open(file_path, 'rb') as f:
        return f.read()

import os


def check_file_not_empty(file_path: str) -> bool:
    if os.path.getsize(file_path) == 0:
        print(f"Ошибка! Файл - {file_path} - пустой")
        return False

    return True

def read_txt_file(file_path: str)->str:
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def write_file_txt(data: str, file_path: str)->None:
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(data)
