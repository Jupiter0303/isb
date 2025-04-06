from decryption import create_key,decoding



def main():
    try:
        with open('cod9.txt', 'r', encoding='utf-8') as file:
            encrypted_data = file.read()
        key = create_key(encrypted_data)
        with open('encryption.txt','w',encoding='utf-8') as file:
            file.write(decoding(encrypted_data,key))
        with open('key.txt','w',encoding='utf-8') as file:
            file.write(str(key))
    except Exception as e:
        print(f"Error: {e} ")


if __name__ == "__main__":
    main()
