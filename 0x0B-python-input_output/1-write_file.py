#!/usr/bin/python3
""" Write Module """


def write_file(filename="", text=""):
    """
        filename: name of file
        text: text to write in
    """
    with open(filename, mode='r+', encoding='utf-8') as f:
        return (f.write(text))
