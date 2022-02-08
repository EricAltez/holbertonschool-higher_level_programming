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

    def test_height(self):
        """ height test """
        self.assertRaises(ValueError, Rectangle, 10, 0)
        self.assertRaises(ValueError, Rectangle, 10, -1)
        self.assertRaises(TypeError, Rectangle, 10, (2, 1))
        self.assertRaises(TypeError, Rectangle, 10, 'a')
        self.assertRaises(TypeError, Rectangle, 10, [1, 2, 3])
        self.assertRaises(TypeError, Rectangle, 10, {'a': 1, 'b': 2})
        self.assertRaises(TypeError, Rectangle, 10, 1.5)
        self.assertRaises(TypeError, Rectangle, 10, 'nan')
        self.assertRaises(TypeError, Rectangle, 10, 'inf')
        self.assertRaises(TypeError, Rectangle, 10, 2.5)
        self.assertRaises(TypeError, Rectangle, 1, 2, 3)
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, 4)
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, 4, 5)

    def test_width(self):
        """ width test """
        self.assertRaises(ValueError, Rectangle, 0, 10)
        self.assertRaises(ValueError, Rectangle, -1, 10)
        self.assertRaises(TypeError, Rectangle, (1, 2), 10)
        self.assertRaises(TypeError, Rectangle, 'a', 10)
        self.assertRaises(TypeError, Rectangle, [1, 2, 3], 10)
        self.assertRaises(TypeError, Rectangle, {'a': 1, 'b': 2}, 10)
        self.assertRaises(TypeError, Rectangle, 1.5, 10)
        self.assertRaises(TypeError, Rectangle, 'nan', 10)
        self.assertRaises(TypeError, Rectangle, 'inf', 10)
        self.assertRaises(TypeError, Rectangle, 2.5, 10)
        self.assertRaises(TypeError, Rectangle, 1, 2, 3)
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, 4)
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, 4, 5)

    def test_x(self):
        """ x test """

    def test_y(self):
        """ y test """
