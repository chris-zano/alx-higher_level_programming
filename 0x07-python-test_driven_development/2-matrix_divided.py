#!/usr/bin/python3
"""
This is the 2-matrix_divided module

This module provides one function matrix_divided
"""


def matrix_divided(matrix, div):
    """
    matrix_divided function divides all elements of a matrix.

    Args:
        matrix (list): a list of lists of the same size of type int or float
        div (int): a number, int or float , cannot be zero 0

    Returns:
        This function returns a new matrix of - a list of lists where all 
        elements of each list is divided by div

    Raises:
        TypeError: matrix is not a list of lists of int or floats
        TypeError: each row of the matrix is not of the same size
        TypeError: div is not a number
        ZeroDivisionError: div is 0
        
    """

    if ((not isinstance(div, int) and not isinstance(div, float))):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if (not isinstance(matrix, list) or matrix == [] or
         not all(isinstance(row, list) for row in matrix) or
         not all(isinstance(n, int) or isinstance(n, float)
             for n in [num for row in matrix for num in row])):
         raise TypeError("matrix must be a matrix (list of lists) of "
                         "integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    return ([list(map(lambda n: round(n / div, 2), row)) for row in matrix])
