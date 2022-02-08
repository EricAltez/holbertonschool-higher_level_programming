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
        for h in [-1, 0]:
            with self.subTest(h=h):
                self.assertRaises(ValueError, Rectangle, h, 2)
        for h in ['a', 'hola', (1, 2), [1, 2, 3], {'a': 1, 'b': 3}, 'nan', 'inf', 2.5]:
            with self.subTest(h=h):
                self.assertRaises(TypeError, Rectangle, h, 2)

    def test_width(self):
        for h in [-1, 0]:
            with self.subTest(h=h):
                self.assertRaises(ValueError, Rectangle, 2, h)
        for h in ['a', 'hola', (1, 2), [1, 2, 3], {'a': 1, 'b': 3}, 'nan', 'inf', 2.5]:
            with self.subTest(h=h):
                self.assertRaises(TypeError, Rectangle, 2, h)

    def test_x(self):
        self.assertRaises(ValueError, Rectangle, 2, 10, -5)
        for x in ['a', 'hola', (1, 2), [1, 2, 3], {'a': 1, 'b': 3}, 'nan', 'inf', 2.5]:
            with self.subTest(x=x):
                self.assertRaises(TypeError, Rectangle, 2, 10, x)

    def test_y(self):
        self.assertRaises(ValueError, Rectangle, 2, 10, 2, -2)
        for y in ['a', 'hola', (1, 2), [1, 2, 3], {'a': 1, 'b': 3}, 'nan', 'inf', 2.5]:
            with self.subTest(y=y):
                self.assertRaises(TypeError, Rectangle, (2, 10, 0, y))
