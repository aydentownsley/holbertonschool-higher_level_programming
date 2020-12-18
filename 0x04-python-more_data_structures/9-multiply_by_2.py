#!/usr/bin/python3
#
# multiply_by_2 - returns a dict
# with values mult by 2
#
# @a_dictionary: dict
#
# Return: new dict


def multiply_by_2(a_dictionary):
    b_dict = dict(a_dictionary)
    for i in b_dict:
        b_dict[i] = b_dict[i] * 2
    return b_dict
