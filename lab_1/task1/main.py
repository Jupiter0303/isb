import constants
from encryption import encryption


def main():
    try:
        with open(constants.KEY_FILE, 'r', encoding='utf-8') as file:
            key = file.read()
        with open(constants.FILE_DATA, 'r', encoding='utf-8') as file:
            data = file.read()
        with open(constants.FILE_ENCRYPTION, 'w', encoding='utf-8') as f:
            f.write(encryption(data, key))
    except Exception as e:
        print(f"Error: {e} ")

if __name__ == "__main__":
    main()