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
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
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
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

    def __str__(self):
        return ('[Square] ({:d}) {:d}/{:d} - {:d}'.format(self.id, self.x,
                self.y, self.width))
