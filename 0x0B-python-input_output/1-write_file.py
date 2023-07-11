#!/usr/bin/python3
"""
This is the 1-write_file.py module
This module provides one function
"""


def write_file(filename="", text=""):
    """
    This function writes to a file

    Args:
        filename (str): name of the file
        text (str): text to be written ot the file
    Returns:
        the number of bytes written
    """

    written_bytes = 0
    if len(filename) > 0:
        with open(filename, "w", encoding="utf-8") as f:
            written_bytes = f.write(text)
    return written_bytes

