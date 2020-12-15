#!/usr/bin/python3
#
# new_in_list - replaces nth element in a list
#
# @my_list: list to be searched
# @idx: location of object to be replaces
#
# Return: new copy of list with replacement
# OR original list if idx is (-) OR out of range


def new_in_list(my_list, idx, element):
    if not my_list:
        return None
    if idx > len(my_list) - 1 or idx < 0:
        return my_list
    a = my_list[:]
    a[idx] = element
    return a
