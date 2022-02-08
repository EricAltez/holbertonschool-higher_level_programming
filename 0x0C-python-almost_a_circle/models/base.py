#!/usr/bin/python3
"""
Base module
"""

import json


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ JSON string representation of list_dictionaries """
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes JSON str repr of list_objs to file """
        aux_l = []
        with open('{}.json'.format(cls.__name__), 'w+') as my_file:
            if list_objs is None:
                my_file.write(cls.to_json_string(aux_l))
            else:
                for item in list_objs:
                    aux_l.append(cls.to_dictionary(item))
                my_file.write(cls.to_json_string(aux_l))
