#!/usr/bin/python3
"""
student class module
"""


class Student:
    """student class"""
    def __init__(self, first_name, last_name, age):
        """ object initialization """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        aux = {}
        if type(attrs) == list:
            for key in attrs:
                if type(key) != str:
                    return self.__dict__
                if key in self.__dict__:
                    aux[key] = self.__dict__[key]
            return aux
        else:
            return self.__dict__

    def reload_from_json(self, json):
        for i in json:
            self.__dict__[i] = json[i]
