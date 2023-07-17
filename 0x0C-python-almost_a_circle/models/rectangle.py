#!/usr/bin/python3
"""
This is the rectangle.py module
This module provides only one class
"""


class Rectangle(Base):
    """
    This is the rectangle class - inherits from the base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle.
        Args:
            width (int): width of the rectangle
            height (int): height of the Rectangle.
            x (int): x coordinate of the Rectangle.
            y (int): y coordinate of the Rectangle.
            id (int): id of Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

