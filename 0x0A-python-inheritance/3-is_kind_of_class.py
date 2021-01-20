#!/usr/bin/python3
""" Type check Module
"""

def is_kind_of_class(obj, a_class):
    """ checks type of object but not
        same object
    """
    if issubclass(type(obj), a_class):
        return True
    return False
