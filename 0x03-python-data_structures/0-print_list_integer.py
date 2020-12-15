#!/usr/bin/python3
#
# print_list_integer - prints a list, one int per line
#
# @my_list: list of ints

def print_list_integer(my_list=[]):
    i = 0
    for i in range(len(my_list)):
        print("{}".format(my_list[i]))
