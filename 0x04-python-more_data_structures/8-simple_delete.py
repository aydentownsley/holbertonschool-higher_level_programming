#!/usr/bin/python3
#
# simple_delete - deletes a key in a dict
#
# @a_dictionary: dict
# @key: dict key
#
# Return: modded dict


def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
