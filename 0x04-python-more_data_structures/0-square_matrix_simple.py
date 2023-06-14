#!/usr/bin/python
def square_matrix_simple(matrix=[]):
    squared_list = []
    for l in matrix:
        sublist = []
        for n in l:
            sublist.append(n ** 2)
        squared_list.append(sublist)
    return squared_list

matrix = []

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)
