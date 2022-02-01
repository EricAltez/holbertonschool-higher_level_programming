#!/usr/bin/python3
"""
append to file module
"""


def append_write(filename="", text=""):
    """ appends string to end fo the file, return number of characters added """
    with open(filename, 'a') as f:
        return f.write(text)
