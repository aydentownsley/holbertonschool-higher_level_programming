#!/usr/bin/python3
""" Read Module """


def read_file(filename=""):
    """
        read and prints a
        UTF8 file
    """
    f = open(filename, mode='r', encoding='utf-8')
    for line in f:
        print(line, end="")
