from constants import stats


def create_encrypted_alphabet(data:str)->list:
    sorted_dict = dict()
    encrypted_alphabet = set(data)
    data_size = len(data)
    for x in encrypted_alphabet:
        sorted_dict[x] = data.count(x)/data_size
    sorted_dict = dict(sorted(sorted_dict.items(), key=lambda item: item[1], reverse=True))
    return list(sorted_dict.keys())


def decoding(data: str, key: dict)->str:
    size = len(key)
    keys = list(key.keys())
    passed_chars = set()
    for index in range(size):
        cur_encrypted_char = keys[index]
        if cur_encrypted_char in passed_chars:
            continue
        if key[cur_encrypted_char] in keys:
            replacement_char = cur_encrypted_char
            while True:
                data = data.replace(key[cur_encrypted_char], '&')
                data = data.replace(replacement_char, key[cur_encrypted_char])
                passed_chars.add(cur_encrypted_char)
                cur_encrypted_char = key[cur_encrypted_char]

                if key[cur_encrypted_char] in keys and not cur_encrypted_char in passed_chars:
                    data = data.replace(key[cur_encrypted_char], '#')
                    data = data.replace('&', key[cur_encrypted_char])
                    cur_encrypted_char = key[cur_encrypted_char]
                else:
                    break

        else:
            data = data.replace(cur_encrypted_char,key[cur_encrypted_char])
            passed_chars.add(cur_encrypted_char)
def swap(data: str, symbol1: str, symbol2: str) -> str:
    data.replace(symbol1,'##&')
    data.replace(symbol2, symbol1)
    data.replace(symbol1, symbol2)
    return data


def decryption(encrypted_text:str)->str:
    encrypted_alphabet = create_encrypted_alphabet(encrypted_text)
    original_alphabet = list(stats.keys())
    print("Формирование ключа:")
    key = dict(zip(encrypted_alphabet,original_alphabet))
    while True:
        print(f"Текущий текст:\n {encrypted_text}")
        print(" Поменять символы - 1 \n Завершить - 2" )
        choice = input().strip()
        if choice == '1':
            while True:
                symbol1 = input("1-ый символ: ").strip()
                symbol2 = input("2-ой символ: ").strip()
                if not (symbol1 in original_alphabet and symbol2 in original_alphabet):
                    print("Некорректно введенный символ, повторите снова.")
                else:
                    encrypted_text = swap(encrypted_text,symbol1,symbol2)

                    break



print(encrypted_text)
    return encrypted_text