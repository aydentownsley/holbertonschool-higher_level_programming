#!/usr/bin/python3
""" checks if exactly same object """


def is_same_class(obj, a_class):
    """
        is same class
    """
    if type(obj) is a_class:
        return True
    return False
