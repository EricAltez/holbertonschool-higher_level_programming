#!/usr/bin/python3
""" rectangle module"""


class Rectangle:
    """create rectangle class"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """define rectangle class elements"""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter for __width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """ Setter for __width """
        if(type(value) != int):
            raise TypeError("widht must be an integer")
        if(value < 0):
            raise ValueError("widht must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Geter for __height """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ Setter for __height """
        if(type(value) != int):
            raise TypeError("height must be an integer")
        if(value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """method: return the rectangle area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """method: returns the rectangle perimeter"""
        if (self.__width == 0 or self.__height == 0):
            return (0)
        else:
            return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        res = ""
        if (self.height == 0 or self.width == 0):
            return(res)
        else:
            for c_idx in range(self.height - 1):
                res += (str(self.print_symbol)*self.width + "\n")
            res += (str(self.print_symbol)*self.width)

        return(res)

    def __repr__(self):
        res = "{}({}, {})".format(type(self).__name__, self.width, self.height)
        return(res)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if isinstance(rect_1, Rectangle):
            if isinstance(rect_2, Rectangle):
                if Rectangle.area(rect_1) >= Rectangle.area(rect_2):
                    return rect_1
                else:
                    return rect_2
            else:
                raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            raise TypeError("rect_1 must be an instance of Rectangle")
