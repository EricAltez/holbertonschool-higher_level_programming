#!/usr/bin/python3
"""
Read file module
"""


def read_file(filename=""):
    """ reads a file """
    with open(filename) as f:
        for line in f:
            print(line)
