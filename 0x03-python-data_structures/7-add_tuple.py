#!/usr/bin/python3
#
# add_tuple - returns a tuple with two ints
#
# @tuple_a: tuple a
# @tuple_b: tuple b
#
# Return: tuple of two ints


def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        a = (0, 0)
    elif len(tuple_a) == 1:
        a = (tuple_a[0], 0)
    elif len(tuple_a) >= 2:
        a = (tuple_a[0], tuple_a[1])

    if len(tuple_b) == 0:
        b = (0, 0)
    elif len(tuple_b) == 1:
        b = (tuple_b[0], 0)
    elif len(tuple_b) >= 2:
        b = (tuple_b[0], tuple_b[1])

    return (a[0] + b[0], a[1] + b[1])
