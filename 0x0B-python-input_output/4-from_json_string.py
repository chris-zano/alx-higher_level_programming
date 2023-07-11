#!/usr/bin/python3
"""
This is the 4-from_json_string.py module
This module provides only one function
"""


def from_json_string(my_str):
    """
    This function returns the json of my_str
    Args:
        my_str (str): string argument
    Returns:
        json of my_str
    """

    import json
    return json.loads(my_str)
