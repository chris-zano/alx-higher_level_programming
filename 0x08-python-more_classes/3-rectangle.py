#!/usr/bin/python3
"""
This is the 0-rectangle module.
This module provides one class
"""


class Rectangle:
    """
    this is the rectangle class
    This class defines a rectangle
    """

    def __init__(self, width=0, height=0):
        """
        this method initialises the class Rectangle object when called.

        Args:
            width (int): the width of the rectangle, optional, default 0
            height (int): the height of the rectangle, optional, default 0

        Returns:
            None

        Raises:
            TypeError if width and height are not integers
            valueError if width and height are less than 0
        """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

        return

    @property
    def width(self):
        """
        getter property for width
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        setter property for width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value
        return

    @property
    def height(self):
        """
        getter property for height
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        setter property for height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
        return

    def area(self):
        """
        returns the area of the rectangle
        """

        if self.__width > 0 and self.__height > 0:
            return self.__width * self.__height
        else:
            return 0

    def perimeter(self):
        """
        returns the perimeter of the rectangle
        """

        if self.__width == 0 or self.__height == 0:
            return 0
        return ((2 * self.__width) + (2 * self.__height))

    def __str__(self):
        """returns printable string representation of the rectangle"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))
        return string
