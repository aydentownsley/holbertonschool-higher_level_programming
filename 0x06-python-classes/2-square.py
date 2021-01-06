#!/usr/bin/python3
""" Square Module """


class Square:
    """ def of square """

    def __init__(self, size=0):
        """ create a square
            size set to zero
            raise Type and Value
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
