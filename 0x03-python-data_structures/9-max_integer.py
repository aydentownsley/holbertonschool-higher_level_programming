#!/usr/bin/python3
#
# max_integer - find largest int in list
#
# @my_list: list to search
#
# Return: biggest int
# OR None if empty list


def max_integer(my_list=[]):
    if not my_list or len(my_list) == 0:
        return None
    a = my_list[0]
    i = 1
    for i in range(len(my_list)):
            if my_list[i] > a:
                a = my_list[i]
    return a
