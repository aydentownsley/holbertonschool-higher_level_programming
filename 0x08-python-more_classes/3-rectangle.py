#!/usr/bin/python3
""" Rectangle Module """


class Rectangle:
    """ Creates Rectangle

        width: 0
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

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
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Calculates the area of Rectangle
            ---
            retreives heigh and width and
            returns the product of the two
        """
        if self.__width is 0 or self.__height is 0:
            return 0
        return self.__height * self.__width

    def perimeter(self):
        """ Caculates the perim of Rectangle
            ---
            retrieves height and width
            mult both by do and return
            the sum.
        """
        if self.width is 0 or self.height is 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        w = self.__width
        h = self.__height
        if h is 0 or w is 0:
            return ''
        return (('#' * w + '\n') * (h - 1) + ('#' * w))
