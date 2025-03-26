

def create_dict_encrypted_text(data:str)->dict:
    sorted_dict_asc = dict()
    encrypted_alphabet = set(data)
    for x in encrypted_alphabet:
        sorted_dict_asc[x] = data.count(x)/len(data)
    sorted_dict_asc = dict(sorted(sorted_dict_asc.items(), key=lambda item: item[1]))
    return sorted_dict_asc


def decryption()->str: