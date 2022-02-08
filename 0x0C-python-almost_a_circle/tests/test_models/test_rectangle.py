#!/usr/bin/python3
""" Rectangle test module """

import unittest
from models.rectangle import Rectangle
from models.base import Base


class RectangleTests(unittest.TestCase):
    """ Rectangle test class"""

    def test_documentation(self):
        """documentation test"""
        self.assertTrue(len(Rectangle.__doc__) > 0)
        self.assertTrue(len(Rectangle.area.__doc__) > 0)
        self.assertTrue(len(Rectangle.display.__doc__) > 0)
        self.assertTrue(len(Rectangle.__str__.__doc__) > 0)
        self.assertTrue(len(Rectangle.update.__doc__) > 0)
        self.assertTrue(len(Rectangle.to_dictionary.__doc__) > 0) 
