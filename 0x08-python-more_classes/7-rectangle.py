#!/usr/bin/python3
""" Rectangle Module """


class Rectangle:
    """ Creates Rectangle

        width: 0
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        type(self).number_of_instances += 1
        self.__width = width
        self.__height = height

    def __del__(self):
        type(self).number_of_instances -= 1
        print('Bye Rectangle...')

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
            raise TypeError("height muse be an integer")
        if value < 0:
            raise ValueError("height myst be >=0")
        self.__height = value

    def area(self):
        """ Calculates the area of Rectangle
            ---
            retreives heigh and width and
            returns the product of the two
        """
        if self.__width is 0 or self.__width is 0:
            return 0
        return self.__height * self.__width

    def perimeter(self):
        """ Caculates the perim of Rectangle
            ---
            retrieves height and width
            mult both by do and return
            the sum.
        """
        if self.__width is 0 or self.__width is 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __repr__(self):
        """ Creates a string rep of Rectangle dimensions
        """
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __str__(self):
        """ Creates a string rep of Rectangle in #
        """
        return (('#' * self.__width + '\n') * (self.__height - 1) +
                ('#' * self.__width))
