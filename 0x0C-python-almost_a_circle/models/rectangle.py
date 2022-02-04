#!/usr/bin/python3
"""

"""

from models.base import Base

class Rectangle(Base):

    @property
    def width(self):
        """ getter for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter fo width """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Geter for __height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for __height """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Geter for __x """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter for __x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ getter for __y"""
        return self.__y

    @y.setter
    def y(self, value):
        """ setter fot y """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def __init__(self, width, height, x=0, y=0, id=None):

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def area(self):
        """ returns the area"""
        return(self.__width * self.__height)

    def display(self):
        """" displays representation using #"""
        for k in range(self.__y):
            print()
        for i in range(self.__height):
            for l in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end='')
            print()

    def __str__(self):
        """ str overriding """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"











