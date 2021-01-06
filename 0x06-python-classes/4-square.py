#!/usr/bin/python3
""" Square Module """


class Square:
    """ def of square """

    def __init__(self, size=0):
        """ create square
            size: size of square (length of side)
            raise:
                Type: if not int
                Value: if < 0
            area: size sqaured
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """ returns size of square """
        return self.__size

    @size.setter
    def size(self, value):
        """ sets size of square """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ returns size squared """
        return self.__size ** 2
