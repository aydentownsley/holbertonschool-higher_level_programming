#!/usr/bin/python3
""" Class to JSON
"""


def class_to_json(obj):
    """
        obj: class to be JSONed
    """
    return (vars(obj))
