#!/usr/bin/python3
"""
This is the 6-load_from_json_file.py module
This module provides only one function
"""


def load_from_json_file(filename):
    """
    This function an object from a json file filename
    Args:
        filename (str): JSON file
    Returns:
        None
    """

    if len(filename) > 0:
        with open(filename, "r", encoding="utf-8") as f:
            data_read = f.read()
            import json
            return json.loads(data_read)
