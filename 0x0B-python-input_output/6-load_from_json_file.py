#!/usr/bin/python3
import json
""" Create Module
"""


def load_from_json_file(filename):
    """
        filename: name of file with
        JSON string
    """
    with open(filename) as f:
        return (json.load(f))
