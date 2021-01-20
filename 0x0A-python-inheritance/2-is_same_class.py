#!/usr/python3
""" checks if exactly same object """

def is_same_class(obj, a_class):
    if a_class is type(obj):
        return True
    return False
