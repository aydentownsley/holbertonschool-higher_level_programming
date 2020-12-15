#!/usr/bin/python3
#
# replace_in_list - replaces item of list at index
#
# @my_list: list to search and modify
# @idx: location to search at
# @element: element to place in list
#
# Return: return list
# OR idx is negative return original list
# OR idx is out of range, return original list


def replace_in_list(my_list, idx, element):
    if idx > len(my_list) or idx < 0:
        return my_list
    for i in range(len(my_list)):
        if i == idx:
            my_list[i] = element
    return my_list
