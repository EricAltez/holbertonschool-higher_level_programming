#!/usr/bin/python3
"""
MyList class module
"""


class MyList(list):
    """ MyList class """

    def print_sorted(self):
        """ prints the list in ascending order """
        for item in self:
            if type(item) != int:
                raise TypeError("item must be an integer")
        print(sorted(self))
