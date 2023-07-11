#!/usr/bin/python3
"""
This is the 3-to_json_string.py
This module provides only one function
"""


def to_json_string(my_obj):
    """
    This function returns the string representation of my_obj
    Args:
        my_obj (any): object
    Returns:
        json string of my_obj
    """

    import json
    return json.dumps(my_obj)
