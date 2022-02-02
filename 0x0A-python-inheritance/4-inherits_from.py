#!/usr/bin/python3
"""
Only sub class of
"""


def inherits_from(obj, a_class):
    """ return true or false """
    if (type(obj) == a_class):
        return False
    return (issubclass(type(obj), a_class))
