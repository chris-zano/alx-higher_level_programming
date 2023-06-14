#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    a = matrix[:]
    return [list(map((lambda n: n * n), sublist)) for sublist in a]
