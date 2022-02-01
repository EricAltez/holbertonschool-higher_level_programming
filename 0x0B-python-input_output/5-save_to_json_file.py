#!/usr/bin/python3
"""
Object to a text file, JSON
"""
import json


def save_to_json_file(my_obj, filename):
    """ writes Object to text file, using JSON rep """
    with open(filename, w+) as f:
        f.write(json.dumps(my_obj))
