#!/usr/bin/python3
""" Pascals Triangle Module
"""


def pascal_triangle(n):
    """
        n: size of triangle
    """
    row = [1]
    triangle = []
    for i in range(n):
        triangle.append(row)
        next_row = []
        next_row.append(row[0])
        for i in range(len(row)-1):
            next_row.append(row[i] + row[i + 1])
        next_row.append(row[-1])
        row = next_row
    return triangle
