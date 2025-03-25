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

    code = list(int(x) for x in key)