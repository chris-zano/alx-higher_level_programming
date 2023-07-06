#!/usr/bin/python3
"""
This is the 101-locked_class module
This module contains one class
"""


class LockedClass:
    """
    This is the LockedClass class of this module

    Attributes:
        __slots__ (list)
    """
    __slots__ = ['first_name']

    def __setattr__(self, name, value):
        """
        This functions sets the attribute of class
        """
        if name != 'first_name':
            raise AttributeError("'LockedClass' object has no "
                                 "attribute '{}'".format(name))
        object.__setattr__(self, name, value)
