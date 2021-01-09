#!/usr/bin/python3
""" Text Indentation Module

Formats a given string,
adding 2 lines after found chars
chars: '.' and '?' and ':'
"""


def text_indentation(text):
    """ text_indentation
        text: given string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    i = 0

    while i < len(text):
        if text[i] in ['.', '?', ':']:
            print(text[i] + '\n')
            if text[i + 1] is ' ':
                i += 1
        else:
            print(text[i], end='')
        i += 1
