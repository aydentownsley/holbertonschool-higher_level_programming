#!/usr/bin/python3
""" Square Module """


class Square:
    """ def of square """

    def __init__(self, size=0):
        """ create square
            size : size of square
        """
        self.__size = size
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    self.__size = size
