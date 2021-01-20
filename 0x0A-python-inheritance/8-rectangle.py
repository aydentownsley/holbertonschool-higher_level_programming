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
        BaseGeometry.integer_validator(self, 'width', width)
        BaseGeometry.integer_validator(self, 'height', height)
        self.__width = width
        self.__height = height
