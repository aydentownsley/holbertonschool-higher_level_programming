#!/usr/bin/python3
""" Rectangle Module """


class Rectangle:
    """ Creates Rectangle

        width: 0
        height: 0
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        type(self).number_of_instances += 1
        self.__width = width
        self.__height = height

    def __del__(self):
        type(self).number_of_instances -= 1
        print('Bye Rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ compares instaces of Rectangles
            ---
            rect_1: rec 1 to compare
            rect_2: rec 2 to compare
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() is rect_2.area():
            return rect_1
        elif rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

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
        if self.__width is 0 or self.__height is 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __repr__(self):
        """ Creates a string rep of Rectangle dimensions
        """
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __str__(self):
        """ Creates a string rep of Rectangle in #
        """
        w = self.__width
        h = self.__height
        s = "{}".format(self.print_symbol)
        return ((s * w + '\n') * (h - 1) + (s * w))
