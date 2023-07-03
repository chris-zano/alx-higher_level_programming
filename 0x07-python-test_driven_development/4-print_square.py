#!/usr/bin/python3
"""
This is the 4-print_square module
This module provides one function print_square
"""


def print_square(size):
    """
    print_square, a function that prints a square with the character #

    Args:
        size (int): the size of the square

    Returns:
        None

    Raises:
        TypeError if size is not an integer
        ValueError if size is less than zero
        TypeError if size is a float and is less than 0
    """

    if (not isinstance(size, int) or isinstance(size, float)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for n in range(size):
        print("#" * size)
