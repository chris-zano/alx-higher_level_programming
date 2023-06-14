#!/usr/bin/python
import sys
def square_matrix_simple(matrix=[]):
    a = matrix[:]
    squared_list = []
    for elmt in a:
        sublist = []
        for n in elmt:
            sublist.append(n ** 2)
        squared_list.append(sublist)
    return squared_list
