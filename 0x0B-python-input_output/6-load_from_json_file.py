#!/usr/bin/python3
""" Create Module
"""
import json


def load_from_json_file(filename):
    """
        filename: name of file with
        JSON string
    """
    with open(filename) as f:
        return (json.load(f))
