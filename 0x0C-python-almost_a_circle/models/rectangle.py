#!/usr/bin/python3
"""
Rectangle module
"""

from models.base import Base
""" import base class """


class Rectangle(Base):
    """ Rectangle class """

    @property
    def width(self):
        """ getter for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for width """
        if type(value) is not int:
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
        if type(value) is not int:
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
        if type(value) is not int:
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
        """ setter for y """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def __init__(self, width, height, x=0, y=0, id=None):
        """ init definition """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """ returns the area"""
        return(self.__width * self.__height)

    def display(self):
        """" displays representation using #"""
        for k in range(self.__y):
            print()
        for i in range(self.__height):
            for m in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end='')
            print()

    def __str__(self):
        """ str overriding """
        ov = f"[Rectangle] ({self.id}) {self.x}/{self.y} -"
        ov += f" {self.width}/{self.height}"
        return ov

    def update(self, *args, **kwargs):
        """ assigns arguments to atributes """
        attri = {0: "id", 1: "width", 2: "height", 3: "x", 4: "y"}
        if args and len(args) > 0:
            if len(args) < 6:
                for i in range(len(args)):
                    setattr(self, attri[i], args[i])
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """ dictionary representation of a Rectangle """
        dic = {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width
        }
        return dic
