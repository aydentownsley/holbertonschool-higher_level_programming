#!/usr/bin/python3
""" Rectangle Module """


class Rectangle:
    """ Creates Rectangle

        width: 0
    """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ return width value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets witdth attr of Rectangle
            ---
            width must be >= 0, and of type
            int
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ return height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets height attr of Rectangle
            ---
            height muse be >= 0, and of
            of type int
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height myst be >= 0")
        self.__height = value
