import json


with open ("settings.json", 'r') as js:
    config = json.load(js)


INITIAL_FILE = config["initial_file"]
ENCRYPTED_FILE = config["encrypted_file"]
DECRYPTED_FILE = config["decrypted_file"]
SYMMETRIC_KEY = config["symmetric_key"]
PUBLIC_PEM = config["public_key"]
PRIVATE_PEM = config["secret_key"]