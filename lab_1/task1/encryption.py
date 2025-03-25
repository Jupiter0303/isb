from math import ceil


def encryption(data:str, key:str)->str:
    height = round(len(data)**0.5)
    width = ceil(len(data)/height)
    data_in_matrix = list( list(data[x*y] for y in range(width)) for x in range(height))
    if height*width > len(data):
        data_in_matrix[height-1] += list('_'*(len(data)-height*width) )