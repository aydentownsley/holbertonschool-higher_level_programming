#!/usr/bin/python3
""" Print Square Module

Prints a square

"""


def print_square(size):
    """ print_square
        size: size of side of square

    """

    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for x in range(size):
        for y in range(size):
            print('#', end="")
        print()
