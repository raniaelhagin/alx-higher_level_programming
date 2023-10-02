#!/usr/bin/python3
""" Module for append_write method
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file

    Args:
        filename (str): filename/path
        text (str): string to be appendded

    Returns:
        number of of characters written
    """
    with open(filename, mode="a", encoding="UTF-8") as file:
        return (file.write(text))
