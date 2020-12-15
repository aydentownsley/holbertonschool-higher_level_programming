#!/usr/bin/python3
#
# element_at - retrieves element at index from list
#
# @my_list: list to search
# @idx: location to search at
#
# Result: return element at location if exists
# OR None if it does not


def element_at(my_list, idx):
    i = 1
    if idx > len(my_list):
        return None
    for i in range(len(my_list)):
        if i == idx:
            return (my_list[i])
