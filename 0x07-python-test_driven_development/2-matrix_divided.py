#!/usr/bin/python3
"""
matrix_divided - function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    args:
        matrix (int, float): the first integer.
        div (int, float): the second integer.
    return: the a matrix with all the nbr divide by div or raise error if fail.
    """

    Error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError(Error_msg)
        if len(matrix[0]) != len(i):
            raise TypeError("Each row of the matrix must have the same size")
    for tab in matrix:
        for nbr in tab:
            if not isinstance(nbr, int) and not isinstance(nbr, float):
                raise TypeError(Error_msg)

    return [[round(nbr / div, 2) for nbr in tab] for tab in matrix]
