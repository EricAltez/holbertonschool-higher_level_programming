#!/usr/bin/python3
"""
MyList class module
"""


class MyList(list):
    """ MyList class """

    def print_sorted(self):
        """ prints the list in ascending order """
        print(sorted(self))
