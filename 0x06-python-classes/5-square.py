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
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Return square area"""
        return (self.__size ** 2)

    def my_print(self):
        if self.size == 0:
            print("")
        else:
            for i in range(self.size):
                print("#" * self.size)
