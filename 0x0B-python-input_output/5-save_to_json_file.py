#!/usr/bin/python3
import json
""" Save Object
"""


def save_to_json_file(my_obj, filename):
    """
        my_obj: object to be saved
        filename: location to save to
    """
    with open(filename) as f:
        return (f.write(json.dumps(my_obj)))
