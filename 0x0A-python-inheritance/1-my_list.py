#!/usr/bin/python3
"""
MyList class module
"""


class MyList(list):
    """ empty class, inherits from list """
    pass

    def print_sorted(self):
        """ prints the list in ascending order """
        print(sorted(self))
