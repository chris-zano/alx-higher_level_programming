#!/usr/bin/python3
"""
This is the 5-text_indentation module
This module provides on function text_indentation
"""


def text_indentation(text):
    """
    This is the text_indentation function
    This function prints a text with 2 new lines 
        after each of these characters: ., ? and :

    Args:
        text (str): the text to indent, madatory argument

    Returns:
        None

    Raises:
        TypeError if text is not a strng
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1



