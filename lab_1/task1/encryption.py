from math import ceil
from constants import COLUMNS

def path_generation( key: str) -> tuple:
    if not key.isdigit():
        raise ValueError("Ключ должен содержать только цифры")
    code = []
    start = 0
    n = len(key)
    while start < n:
        end = start
        while end < n and int(key[start:end + 1]) < COLUMNS:
            end += 1
        if end == start:
            start += 1
            continue
        num = int(key[start:end])
        code.append(num)
        start = end
    return tuple(code)


def encryption(original_data:str, key:str)->str:
    data = original_data.replace(" ","")
    data = data.replace("!","")
    data = data.replace("?","")
    data = data.replace("—","")
    data = data.replace("-","")
    data = data.replace(".","")
    data = data.replace(",","")
    data = data.replace(";","")
    data = data.replace(":","")
    data = data.replace("\n","")
    data = data.replace("(","")
    data = data.replace(")","")
    data = data.lower()

    width = COLUMNS
    height = ceil(len(data)/width)
    data_in_matrix = []
    for x in range(height):
        data_in_matrix.append([])
        for y in range(width):
            index = x * width + y
            if(index < len(data)):
                data_in_matrix[x].append(data[index])

            else:
                data_in_matrix[x].append('_')
    code = path_generation(key)
    print(code, width, height)
    encrypted_data = ''
    for x in range(height):
        for y in code:
            if not data_in_matrix[x][y] == '_':
                encrypted_data+= data_in_matrix[x][y]
    return encrypted_data