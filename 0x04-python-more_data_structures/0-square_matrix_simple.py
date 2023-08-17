#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """computes the square value of all integers of a matrix"""

    squared_matrix = []

    for i in range(len(matrix)):
        squared_matrix.append(list(map(lambda x: x**2, matrix[i])))

    return (squared_matrix)
