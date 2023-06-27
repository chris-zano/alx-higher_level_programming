#!/usr/bin/python3
"""
6-square.py
"""


class Square:
    """
    Creates a square and defines a square based on optional size
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        creates an instance of the square
        Args:
            size: size of the square
            position: coordinates of the square
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")

        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if not (isinstance(value[0], int) and isinstance(value[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")

        if not (value[0] >= 0 and value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__size = size
        self.__position = position

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
        return

    @property
    def position(self):
        """
        getter to retreive the position of the square
        """

        return self.__position

    @position.setter
    def position(self, value):
        """
        position setter to set the coordinates of a square
        Args:
            value: new coordinates for the square
        """

        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")

        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if not (isinstance(value[0], int) and isinstance(value[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")

        if not (value[0] >= 0 and value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

        return

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
            return

        for i in range(self.__position[1]):
            print()

        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

        return
