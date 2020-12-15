#!/usr/bin/python3
#
# print_matrix_integer - print matrix
#
# @matrix: double list
#
# Return: void


def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print('{:d}'.format(matrix[i][j]), end=" ")
        print()
