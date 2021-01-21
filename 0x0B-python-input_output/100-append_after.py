#!/usr/bin/python3
""" Search and Place
"""


def append_after(filename="", search_string="", new_string=""):
    """
        Search for text string in file
        and append new text at end of
        line
    """
    with open(filename, 'r+') as f:
        for line in f:
            if search_string in line:
                print(line, end='')
                print(new_string, end='')
            else:
                print(line, end='')
