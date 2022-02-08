#!/usr/bin/python3
""" BaseTest module """


from models.base import Base
import unittest


class BaseTest(unittest.TestCase):
    """ BaseTest class """

    def test_asign_autoid(self):
        """ test auto id asignation """
        a = Base()
        b = Base()
        c = Base()
        d = Base()
        e = Base()
        f = Base()
        g = Base()

        self.assertEquals(a.id, 1)
