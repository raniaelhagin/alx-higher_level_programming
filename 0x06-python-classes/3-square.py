#!/usr/bin/python3
"""Create a Square class."""


class Square:
    """Square class"""

    def __init__(self, size=0):
        """
        Class inistanciation

        Args:
            size (int): private instance attribute, size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Return square area"""
        return (self.__size ** 2)