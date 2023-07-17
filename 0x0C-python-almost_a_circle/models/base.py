#!/usr/bin/python3
"""
This is the base.py model
This model provides only one class Base
This class will be the “base” of all other classes in this project
"""


class Base:
    """
    This is the base class
    The goal of it is to manage id attribute in all your future classes
    and to avoid duplicating the same code

    Attributes:
        Private: __nb_objects(int)
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new Base.
        Args:
            id (int): The id of the new Base instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
