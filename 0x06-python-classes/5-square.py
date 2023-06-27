#!/usr/bin/python3
"""
5-square.py
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

    @property
    def size(self):
        """
        getter property to retrieve the size of the square
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        setter to set the value of the size of the square
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        returns the computed value of the area
        """

        return self.__size ** 2

    def my_print(self):
        """
        prints the square with size using #
        """

        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("#" * self.__size)

        return
