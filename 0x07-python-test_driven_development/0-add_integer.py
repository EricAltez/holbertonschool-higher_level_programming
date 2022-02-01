#!/usr/bin/python3
"""
function: add 2 int
return: int
"""


def add_integer(a, b=98):
    """ args must be int or float """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    return int(a + b)
