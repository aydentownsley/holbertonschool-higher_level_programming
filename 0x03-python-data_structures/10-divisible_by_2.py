#!/usr/bin/python3
#
# divisible_by_2 - finds all mutliples
# of 2 in a list
#
# @my_list: list to search
#
# Return: List of True/False values
# depending on divisible by 2


def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    a = list(my_list)
    for i in my_list:
        if my_list[i] % 2 == 0:
            a[i] = True
        else:
            a[i] = False

    return a
