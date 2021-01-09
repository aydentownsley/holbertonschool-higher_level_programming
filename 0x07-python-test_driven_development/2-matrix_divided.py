#!/usr/bin/python3
"""
Divide Matrix Module

Divides elements of a matrix
"""


def matrix_divided(matrix, div):
    """ matrix_divided
        matrix: matrix of ints
        div: int to divide matrix by """

    a = "matrix must be a matrix (list of lists) of integers/floats"
    b = "Each row of the matrix must have the same size"

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")

    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if (type(matrix[x][y]) is not int and
                    type(matrix[x][y]) is not float):
                raise TypeError(a)
    for r in range(len(matrix)):
        if r < len(matrix) - 1:
            if len(matrix[r]) != len(matrix[r + 1]):
                raise TypeError(b)

    new_matrix = [[round(i/div, 2) for i in row] for row in matrix]
    return new_matrix
