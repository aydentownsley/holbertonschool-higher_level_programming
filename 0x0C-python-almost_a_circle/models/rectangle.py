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
        self.id = super().__init__(id)

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
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                print('#', end='')
            if i < (self.__height):
                print()
