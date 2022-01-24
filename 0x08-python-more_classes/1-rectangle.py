#!/usr/bin/python3
""" 
rectangle module
"""


class Rectangle:
    """create rectangle class"""

    def __init__(self, width=0, height=0):
        """define rectangle class elements"""

        self.height = height
        self.width = width

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if(type(value) != int):
            raise TypeError("widht must be an integer")
        if(value < 0):
            raise ValueError("widht must be >= 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if(type(value) != int):
            raise TypeError("height must be an integer")
        if(value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value
