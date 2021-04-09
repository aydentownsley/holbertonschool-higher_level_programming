#!/usr/bin/python3
""" find peak """

def find_peak(list_of_integers):
    """ find peak in list

    Args:
        list_of_integers

    return: peak
    """
    l = list_of_integers
    peak = None
    for i in range(0, len(l)):
        if i == 0 and len(l) > 1 and l[i + 1] < l[i]:
            return l[i]
        elif i > 0 and l[i] >= l[i - 1] and l[i] >= l[i + 1]:
            return l[i]
