#!/usr/bin/python3
""" Module for write_file method
"""

def write_file(filename="", text=""):
    """Writes a text to a file

    Args:
        filename (str): filename/path
        text (str): string to be written

    Returns:
        number of of characters written
    """
    with open(filename, mode="w", encoding="UTF-8") as file:
        return (file.write(text))
