from constants import stats as original_alphabet

def create_dict_encrypted_text(data:str)->dict:
    sorted_dict_asc = dict()
    encrypted_alphabet = set(data)
    for x in encrypted_alphabet:
        sorted_dict_asc[x] = data.count(x)/len(data)
    sorted_dict_asc = dict(sorted(sorted_dict_asc.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict_asc


def decryption(encrypted_text:str)->str:
    encrypted_text.replace('\n','')
    encrypted_alphabet = create_dict_encrypted_text(encrypted_text)
    encrypted_alphabet_keys = encrypted_alphabet.keys()
    original_alphabet_keys = original_alphabet.keys()
    encrypted_text.replace(encrypted_alphabet[encrypted_alphabet_keys[0]],
                           original_alphabet_keys[0])
    start1 = 1
    start2 = 1
    while(start1 < len(encrypted_alphabet_keys)
          and start2 < len(original_alphabet_keys)):
        print(encrypted_text)
        print (Выберет дей)