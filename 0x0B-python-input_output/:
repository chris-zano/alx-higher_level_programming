#!/usr/bin/python3
"""
This is the 5-save_to_json_file.py module
This module provides only one function
"""


def save_to_json_file(my_obj, filename):
    """
    This function save my_obj as json to filename
    Args:
        my_obj (any): pyton object
        filename (str): filename as a text file
    Retuns:
        None
    """

    if len(filename) > 0:
        with open(filename, "w", encoding="utf-8") as f:
            import json
            json.dump(my_obj, f)
