#!/usr/bin/python3
""" rectangle module"""


class Rectangle:
    """create rectangle class"""

    def __init__(self, height=0, width=0):
        """define rectangle class elements"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """getter for __width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """ Setter for __width """
        if(type(value) != int):
            raise TypeError("width must be an integer")
        if(value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter for __height """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ Setter for __height """
        if(type(value) != int):
            raise TypeError("height must be an integer")
        if(value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value
