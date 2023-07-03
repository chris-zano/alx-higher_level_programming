#!/usr/bin/bash
"""
This is the 0-add_integer module

This module provides one function def add_integer(a, b=98):
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
    """

    if type(a) is not int or type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int or type(b) is not float:
        raise TypeError("b must be an integer")
    
    a = int(a)
    b = int(b)

    return int(a + b)
