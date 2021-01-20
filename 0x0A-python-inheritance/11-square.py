#!/usr/bin/python3
""" BaseGeo Module """


class BaseGeometry:
    """ base geo class
    """

    def area(self):
        """
            self
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ int validate
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be an integer".format(name))


class Rectangle(BaseGeometry):
    """ Rectangle
    """

    def __init__(self, width, height):
        """ init
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """ returns width * height
        """
        return (self.__width * self.__height)

    def __str__(self):
        """ String form
        """
        return ("[Retangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    """ Square
    """

    def __init__(self, size):
        """ init
        """
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ return size squared
        """
        return (self.__size ** 2)

    def __str__(self):
        """ makes it stringy
        """
        return ("[Square] {}/{}".format(self.__size, self.__size))
