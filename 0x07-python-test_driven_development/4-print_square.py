#!/usr/bin/python3
# Author: Rania Hamada

""" This module contais a function prints a square with the character # """


def print_square(size):
    """ prints a square with the character #

    Args:
        size (int):  length of the square

    Raises:
        TypeError: if size is not an integer (float and < 0)
        ValueError: if size < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
