#!/usr/bin/python3
""" JSON Module



"""
import json


def to_json_string(my_obj):
    """
        my_obj: obj to be
        interpretted as str
    """
    return (json.dumps(my_obj))
