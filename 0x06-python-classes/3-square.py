#!/usr/bin/python3
""" Square Module """


class Square:
    """ def of square """

    def __init__(self, size=0):
        """ create square
            size: size of square
            raise:
                Type: if not int
                Value: if < 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ returns size squared """
        return self.__size ** 2
