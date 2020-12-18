#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    test = matrix[:]
    for x in range(len(matrix)):
        test[x] = list(map(lambda i: i * i, matrix[x]))
    return test
