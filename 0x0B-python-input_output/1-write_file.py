#!/usr/bin/python3
"""
write to file module
"""


def write_file(filename="", text=""):
    """ writes string, return number of characters written"""
    with open(filename, 'w') as f:
        return f.write(text)
