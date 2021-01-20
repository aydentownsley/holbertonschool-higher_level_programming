#!/usr/bin/python3
""" BaseGeo Module """


class BaseGeometry:
    """ base geo class
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be an integer".format(name))
