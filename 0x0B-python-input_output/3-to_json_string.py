#!/usr/bin/python3
import json
""" JSON Module
"""


def to_json_string(my_obj):
    """
        my_obj: obj to be
        interpretted as str
    """
    return (json.dumps(my_obj))
