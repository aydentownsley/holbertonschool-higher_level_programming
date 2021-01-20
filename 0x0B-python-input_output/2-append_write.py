#!/usr/bin/python3
""" Append Module
"""


def append_write(filename="", text=""):
    """
        filename: name of file
        text: text to append
    """
    with open(filename, mode='a', encoding='utf-8') as f:
        return(f.write(text))
