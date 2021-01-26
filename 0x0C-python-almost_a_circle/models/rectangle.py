#!/usr/bin/python3
"""
First Rectangle Module
-------
This module inherits from Base
and then adds private attributes
- WIDTH
- HEIGHT
- X
- Y
Each with its own getter
and setter
"""
from models.base import Base


class Rectangle(Base):
    """
        Rectangle: Object from Base
        Width: __width
        Height: __height
        x: __x
        y: __y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        id = super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, val):
        if type(val) is not int:
            raise TypeError("width must be an integer")
        elif val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, val):
        if type(val) is not int:
            raise TypeError("height must be an integer")
        elif val <= 0:
            raise ValueError("height must be > 0")
        self.__height = val

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        if type(val) is not int:
            raise TypeError("x must be an integer")
        elif val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        if type(val) is not int:
            raise TypeError("y must be an integer")
        elif val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def area(self):
        return self.__width * self.__height

    def display(self):
        for g in range(0, self.__y):
                print()
        for i in range(0, self.__height):
            for h in range(0, self.__x):
                print(' ', end='')
            for j in range(0, self.__width):
                print('#', end='')
            if i < (self.__height):
                print()

    def __str__(self):
        return ('[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}'.format(self.id,
                self.__x, self.__y, self.__width, self.__height))

    def to_dictionary(self):
        return {'id' : self.id, 'width' : self.width, 'height' : self.height,
                'x' : self.x, 'y' : self.y}

    def update(self, *args, **kwargs):
        if args:
            n_arg = len(args)

        if args and n_arg != 0:
            if n_arg > 0:
                self.id = args[0]
            if n_arg > 1:
                self.width = args[1]
            if n_arg > 2:
                self.height = args[2]
            if n_arg > 3:
                self.x = args[3]
            if n_arg > 4:
                self.y = args[4]
        else:
            if 'id' in kwargs:
                self.id = kwargs.get('id')
            if 'width' in kwargs:
                self.width = kwargs.get('width')
            if 'height' in kwargs:
                self.height = kwargs.get('height')
            if 'x' in kwargs:
                self.x = kwargs.get('x')
            if 'y' in kwargs:
                self.y = kwargs.get('y')
