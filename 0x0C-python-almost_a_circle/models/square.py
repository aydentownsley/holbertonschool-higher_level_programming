#!/usr/bin/python3
"""
Square Module
-------
This creates a square
object using the rectangle
Module to inherit attrs.
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Square: inherited from Rectangle
        -----
        width: side
        height: side
        * for square both will be the same
    """
    def __init__(self, size, x=0, y=0, id=None):
            super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ gets size (side) of square """

        return self.width

    @size.setter
    def size(self, value):
        """
            sets size value
            ---
            self: object
            value: value to be validated
            through both witdth and height
            inherited from rectangle
        """

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
            updates attributes of instance
            ---
            self: object
            *args: attrs of square (list)
            *kwargs: attrs of square (dict)
        """
        if args:
            n_arg = len(args)

        if args and n_arg != 0:
            if n_arg > 0:
                self.id = args[0]
            if n_arg > 1:
                self.width = args[1]
            if n_arg > 2:
                self.x = args[2]
            if n_arg > 3:
                self.y = args[3]
        else:
            if 'id' in kwargs:
                self.id = kwargs.get('id')
            if 'size' in kwargs:
                self.width = kwargs.get('size')
                self.height = kwargs.get('size')
            if 'x' in kwargs:
                self.x = kwargs.get('x')
            if 'y' in kwargs:
                self.y = kwargs.get('y')

    def to_dictionary(self):
        """ makes dictionary from attrs of instance """

        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

    def __str__(self):
        """ creates string representation of object """

        return ('[Square] ({:d}) {:d}/{:d} - {:d}'.format(self.id, self.x,
                self.y, self.width))
