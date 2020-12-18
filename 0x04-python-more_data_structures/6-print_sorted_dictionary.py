#!/usr/bin/python3
#
# print_sorted_dictionary - print dict of ordered keys
#
# @a_dictionary: dictionary
#
# Return: print


def print_sorted_dictionary(a_dictionary):
    for i in sorted(a_dictionary.keys()):
        print('{:s}: {}'.format(i, a_dictionary[i]))
