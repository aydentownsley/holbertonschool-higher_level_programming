#!/usr/bin/python3
#
# only_diff_elements - return elements that are unique to only one set
#
# @set_1: set
# @set_2: set
#
# Return: set of unique elements


def only_diff_elements(set_1, set_2):
    return set_1.symmetric_difference(set_2)
