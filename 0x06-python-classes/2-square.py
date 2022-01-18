#!/usr/bin/python3
"""
Hamer time!!
"""


class Square:
    """
    Square class
    """

    def __init__(self, size=0):
        """
        Define class elements
        """
        if(type(size) != int):
            raise TypeError("size must be an integer")
        if(size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
