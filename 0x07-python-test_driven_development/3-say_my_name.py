#!/usr/bin/python3
# Author: Rania Hamada

""" This module contais a function that prints name """


def say_my_name(first_name, last_name=""):
    """ prints name

    Args:
        first_name (str): first name
        last_name (str): last name

    Raises:
        TypeError: if first_name or last_name aren't strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
