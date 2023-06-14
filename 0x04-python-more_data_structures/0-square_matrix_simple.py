#!/usr/bin/python
def square_matrix_simple(matrix=[]):
    squared_list = []
    for elmt in matrix:
        sublist = []
        for n in elmt:
            sublist.append(n ** 2)
        squared_list.append(sublist)
    return squared_list
