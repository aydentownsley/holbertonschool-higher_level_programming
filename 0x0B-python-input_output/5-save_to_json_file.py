#!/usr/bin/python3
""" Save Object
"""
import json


def save_to_json_file(my_obj, filename):
    """
        my_obj: object to be saved
        filename: location to save to
    """
    with open(filename, 'w') as f:
        return (f.write(json.dumps(my_obj)))
