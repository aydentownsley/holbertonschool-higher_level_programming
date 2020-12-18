#!/usr/bin/python3
#
# uniq_add - adds all unique ints in a list
# only once for each occurence
#
# @my_list: passed int list
#
# Return: sum


def uniq_add(my_list=[]):
    sum_list = set(my_list[:])
    sumof = 0
    for i in sum_list:
        sumof = sumof + i
    return sumof
