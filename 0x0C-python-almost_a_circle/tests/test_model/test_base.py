#!/usr/bin/python3
""" Base tests module"""
import unittest
from models.base import Base

class BaseTests(unittest.TestCase):
    """ Base Model test class """
    def test_initialization(self):
        """ initialization of base class tests """
        a = Base()
        self.assertAlmostEquals(a.id, 1)
        b = Base(4)
        self.assertAlmostEquals(b.id, 4)
        b.id = -4
        self.assertAlmostEquals(b.id, -4)
        c = Base()
        self.assertAlmostEquals(c.id, 3)
