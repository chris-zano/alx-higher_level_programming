#!/usr/bin/python
def square_matrix_simple(matrix=[]):
    return [list(map((lambda n: n * n), sublist)) for sublist in matrix]
