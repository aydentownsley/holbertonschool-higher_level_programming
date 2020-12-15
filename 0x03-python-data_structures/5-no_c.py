#!/usr/bin/python3
#
# no_c - removes c and C from a string
#
# @my_string: string to edit
#
# Return: modified string
# OR None if string doesnt exist


def no_c(my_string):
    if not my_string:
        return None
    return my_string.translate({ord(i): None for i in 'cC'})
