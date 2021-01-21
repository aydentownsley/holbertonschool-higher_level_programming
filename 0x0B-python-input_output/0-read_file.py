#!/usr/bin/python3
""" Read Module """


def read_file(filename=""):
    """
        read and prints a
        UTF8 file
    """
    with open(filename, mode='r', encoding='utf-8') as f:
            print(f.read(), end='')
