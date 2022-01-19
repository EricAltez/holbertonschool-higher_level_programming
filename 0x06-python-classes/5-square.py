#!/usr/bin/python3
""" Square module """


class Square:
    """ Square class creation """

    def __init__(self, size=0):
        """ Define class elements """
        if(type(size) != int):
            raise TypeError("size must be an integer")
        if(size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Define area Method, return the area """
        return self.__size * self.__size

    @property
    def size(self):
        """ Geter for __size """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ Setter for __size """
        if(type(value) != int):
            raise TypeError("size must be an integer")
        if(value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """ Print a aquare """
        if(self.__size == 0):
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
