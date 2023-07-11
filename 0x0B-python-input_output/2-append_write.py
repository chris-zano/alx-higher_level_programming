#!/usr/bin/python3
"""
This is the 2-append_write.py module
This module provides only one function
"""


def append_write(filename="", text=""):
    """
    This function appends text to filename
    Args:
        filename (str): name of the file
        text (str): text to append
    Returns:
        number of characters added
    """

    added_bytes = 0
    if len(filename) > 0:
        with open(filename, "a", encoding="utf-8") as f:
            added_bytes = f.write(text)
    return added_bytes
