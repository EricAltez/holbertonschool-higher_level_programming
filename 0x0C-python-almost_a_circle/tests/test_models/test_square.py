#!/usr/bin/python3
""" Rectangle test module """
import unittest
from models.square import Square


class SquareTests(unittest.TestCase):
    """ Square test class"""

    def test_initialization(self):
        """ test init """

 Square= Rectangle(4, 2)
        res_list = [2, 4, 0, 0, 1]
        rec_list = [r.height, r.width, r.x, r.y, r.id]
        self.assertAlmostEqual(rec_list, res_list)

        r2 = Rectangle(2, 2, 2, 2)
        res_list = [2, 2, 2, 2, 2]
        rec_list = [r2.height, r2.width, r2.x, r2.y, r2.id]
        self.assertAlmostEqual(rec_list, res_list)
