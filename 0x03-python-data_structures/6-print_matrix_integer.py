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
            if j == len(matrix[i]) - 1:
                print('{:d}'.format(matrix[i][j]), end="")
            else:
                print('{:d}'.format(matrix[i][j]), end=" ")
        print()
