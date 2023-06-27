#!/usr/bin/python3
"""
2-square.py
"""


class Square:
    """
    Creates a square and defines a square based on optional size
    """

    def __init__(self, size=0):
        """
        creates an instance of the square
        Args:
            size: size of the square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
