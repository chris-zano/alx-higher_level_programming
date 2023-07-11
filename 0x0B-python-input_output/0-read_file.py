#!/usr/bin/python3
"""
This is the 0-read_file.py module
This module provides only one function
"""


def read_file(filename=""):
    """
    This function reads a text file and prints it to stdout

    Args:
        filename (str): name of the file to be read

    Returns:
        None
    """

    if len(filename) > 0:
        with open(filename, "r", encoding="utf-8") as f:
            read_data = f.read()
            print(read_data, end="")
    return
