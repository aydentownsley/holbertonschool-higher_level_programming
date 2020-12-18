#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = [[i*i for i in row] for row in matrix]
    return result
