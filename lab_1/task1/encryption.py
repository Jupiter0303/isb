from math import ceil


def encryption(original_data:str, key:str)->str:
    data = original_data.replace(" ","")
    height = round(len(data)**0.5)
    width = ceil(len(data)/height)
    data_in_matrix = []
    for x in range(height):
        data_in_matrix.append([])
        for y in range(width):
            index = x * width + y
            if(index < len(data)):
                data_in_matrix[x].append(data[index])

            else:
                data_in_matrix[x].append('_')
    code = tuple(int(x) for x in key)
    encrypted_data = ''
    for x in range(height):
        for y in code:
            if not data_in_matrix[x][y] == '_':
                encrypted_data+= data_in_matrix[x][y]
    return encrypted_data