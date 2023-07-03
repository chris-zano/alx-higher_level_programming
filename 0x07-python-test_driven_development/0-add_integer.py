#!/usr/bin/python3
"""
This is the 0-add_integer module

This module provides one function add_integer
"""


def add_integer(a, b=98):
    """
    This is the add_integer function.
    This function adds two intergers and returns the result

    Args:
        a (int): The first argument of this function...it is mandatory
        b (int): The second argument...it is optional, it defaults to 98

    Returns:
        This function returns an integer sum of a and b
        if b is not provided, it return a + 98

    Raises:
        TypeError when a or b are neither int nor float
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
