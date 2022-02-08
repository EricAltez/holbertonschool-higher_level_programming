#!/usr/bin/python3
""" Base tests module"""
import unittest
from models.base import Base

class BaseTests(unittest.TestCase):
    """ Base Model test class """

    def test_no_args(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)
