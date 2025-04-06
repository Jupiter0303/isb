from constants import stats


def create_encrypted_alphabet(data:str)->list:
    sorted_dict = dict()
    encrypted_alphabet = set(data)
    data_size = len(data)
    for x in encrypted_alphabet:
        sorted_dict[x] = data.count(x)/data_size
    sorted_dict = dict(sorted(sorted_dict.items(), key=lambda item: item[1], reverse=True))
    return list(sorted_dict.keys())

def swap(symbol1:str,symbol2:str,key:dict)->dict:
    swap_keys = list()
    for k in key:
        if key[k] == symbol1 or key[k] == symbol2:
            swap_keys.append(k)
        if len(swap_keys) == 2:
            break
    key[swap_keys[0]],key[swap_keys[1]] = key[swap_keys[1]],key[swap_keys[0]]
    return key


def decoding(encrypted_data: str, key: dict)->str:
    decrypted_data = list()
    for char in encrypted_data:
        if char in key:
            decrypted_data.append(key[char])
        else:
            raise KeyError(f"Символ {char} отсутствует в словаре key в функции decoding")
    return ''.join(decrypted_data)


def create_key(encrypted_text:str)->dict:
    encrypted_alphabet = create_encrypted_alphabet(encrypted_text)
    original_alphabet = list(stats.keys())
    print("Формирование ключа:")
    key = dict(zip(encrypted_alphabet,original_alphabet))
    while True:
        print(f"Текущий текст:\n {decoding(encrypted_text,key)}")
        print(f"Текущий ключ:\n {key}")

        print(" Поменять символы - 1 \n Завершить - любой другой символ" )
        choice = input().strip()
        if choice == '1':
            symbol1 = input("1-ый символ: ").strip()
            symbol2 = input("2-ой символ: ").strip()
            while not (symbol1 in original_alphabet and symbol2 in original_alphabet):
                print("Некорректно введенный символ, повторите снова.")
                symbol1 = input("1-ый символ: ").strip()
                symbol2 = input("2-ой символ: ").strip()
            key = swap(symbol1,symbol2,key)
        else:
            break
    return key

