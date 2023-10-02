#!/usr/bin/python3
# Author: Rania Hamada

""" This module contais a function prints
text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """ prints text with 2 new lines

    Args:
        text (string):  string to be printed

    Raises:
        TypeError: if text is not an string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chr = 0
    while chr < len(text) and text[chr] == ' ':
        chr += 1

    while chr < len(text):
        print(text[chr], end="")
        if text[chr] == "\n" or text[chr] in ".?:":
            if text[chr] in ".?:":
                print("\n")
            chr += 1
            while chr < len(text) and text[chr] == ' ':
                chr += 1
            continue
        chr += 1
