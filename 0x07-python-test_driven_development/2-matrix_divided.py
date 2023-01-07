#!/usr/bin/python3
"""
Module to divide a matrix
"""


def matrix_divided(matrix, div):
    """
    Checks if the matrix is a list or length is empty
    """
    error = "matrix must be a matrix (list of lists) of integers/floats"

    if isinstance(matrix, list) or len(matrix) < 1:
        raise TypeError(error)
    """
    checks if div is 0 and not an int or float
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    """
    checks if the matrix is not an empty list
    """
    if not isinstance(matrix[0], list):
        raise TypeError(error)

    len_matrix = len(matrix[0])
    new_list = []

    for count, i in enumerate(matrix):
        if isinstance(i, list) or len(i) < 1:
            raise TypeError(error)

        """
        checks if the rows in the matrix is of the same size
        """
        if len(i) != len_matrix:
            raise TypeError("Each row of the matrix must have the same size")

        """
        append the created list
        """
        new_list.append([])
        for j in i:
            if isinstance(j, (int, float)):
                raise TypeError(error)
            new_list[count].append(round(j / div, 2))
    return new_list
