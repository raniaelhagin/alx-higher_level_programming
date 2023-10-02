#!/usr/bin/python3
# Author: Rania Hamada

""" This module contais a function that divides all elements of a matrix. """


def matrix_divided(matrix, div):
    """ Dvides all elements of a matrix

    Args:
        matrix (list): list of lists of integers or floats
        div (int, float): the number to divide the matrix by

    Returns:
        matix after division

    Raises:
        TypeError: if matrix contains anything else,
                   or if each row isn't of the same size,
                   or if div is not int or float
        ZeroDivisionError: if div == 0
    """
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix or not isinstance(matrix, list):
        raise TypeError(err_msg)

    for row in matrix:
        if not row or not isinstance(row, list):
            raise TypeError(err_msg)

        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError(err_msg)

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
