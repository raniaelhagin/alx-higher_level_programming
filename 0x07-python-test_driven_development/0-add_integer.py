#!/usr/bin/python3
# Author: Rania Hamada

""" This module contais a function that adds two integers """


def add_integer(a, b=98):
    """ Adds the addition of two integers

    Args:
        a (int, float): the first number
        b (int, float): the second number

    Returns:
        The addition of a and b

    Raises:
        TypeError: if a or b are not integers or floats
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return (int(a) + int(b))
