#!/usr/bin/python3
""" Square Module """


class Square:
    """ def of square """

    def __init__(self, size=0, position=(0, 0)):
        """ create square
            size: size of square (length of side)
            raise:
                Type: if not int
                Value: if < 0
            area: size sqaured
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self, value):
        """ get pos """
        return self.__position

    @position.setter
    def position(self, value):
        """ set pos """
        self.__postition = value
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tulpe of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tulpe of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tulpe of 2 positive integers")

    def area(self):
        """ returns size squared """
        return self.__size ** 2

    def my_print(self):
        """ prints square """
        if self.__size == 0:
            print()
        else:
            for ypos in range(self.__position[1]):
                print()
            for x in range(self.__size):
                for xpos in range(self.__position[0]):
                    print(" ", end="")
                for y in range(self.__size):
                    print("#", end="")
                print()
