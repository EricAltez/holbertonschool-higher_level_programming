#!/usr/bin/python3
"""

"""

from models.base import Base

class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ getter for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter fo width """
        self.__width = value

    @property
    def height(self):
        """ Geter for __height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for __height """
        self.__height = value

    @property
    def x(self):
        """ Geter for __x """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter for x"""
        self.__x = value

    @property
    def y(self):
        """ getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """ setter fot y """
        self.__y = value








