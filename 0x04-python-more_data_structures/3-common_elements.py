#!/usr/bin/python3
#
# common_elements - returns common elements in two sets
#
# @set_1: set to search
# @set_2: set to search
#
# Return: common elements


def common_elements(set_1, set_2):
    if (set_1 & set_2):
        return set(set_1 & set_2)
