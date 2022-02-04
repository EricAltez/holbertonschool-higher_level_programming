#!/usr/bin/python3
"""

"""


class Base:

    def __init__(self, id=None):

        __nb_objects = 0
        if id != None:
            id = None
        else:
            __nb_objects += 1
            id = __nb_objects
