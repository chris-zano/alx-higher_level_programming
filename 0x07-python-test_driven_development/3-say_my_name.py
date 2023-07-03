#!/usr/bin/python3
"""
This is the 3-say_my_name module.
This module provides one function say_my_name
"""


def say_my_name(first_name, last_name=""):
    """
    Function: say_my_name
        prints(My name is <first name> <last name>)

    Args:
        first_name (str):input argument, madatory, firstname
        last_name (str): input argument, optional, lastname

    Returns:
        None

    Raises: 
        TypeError if input arguments are not instances of the string class
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if not first_name:
        raise TypeError("say_my_name() missing 1 required positional "
                        "argument: 'first_name'")
    print("My name is {} {}".format(first_name, last_name))

    return
