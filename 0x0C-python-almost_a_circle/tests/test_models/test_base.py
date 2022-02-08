#!/usr/bin/python3
""" BaseTest module """

from models.rectangle import Rectangle
from models.base import Base
import unittest


class BaseTest(unittest.TestCase):
    """ BaseTest class """

    def test_asign_autoid(self):
        """ test auto id asignation """
        a = Base()
        b = Base(15)
        c = Base()
        d = Base()
        e = Base(11)
        f = Base()
        g = Base(-15)
        h = Base(89)

        self.assertEquals(a.id, 1)
        self.assertEquals(b.id, 15)
        self.assertEquals(c.id, 2)
        self.assertEquals(d.id, 3)
        self.assertEquals(e.id, 11)
        self.assertEquals(f.id, 4)
        self.assertEquals(g.id, -15)
        self.assertEquals(h.id, 89)
        h = Base(98)
        self.assertEquals(h.id, 98)

    def test_documentation(self):
        self.assertTrue(len(Base.__doc__) > 0)
        self.assertTrue(len(Base.to_json_string.__doc__) > 0)
        self.assertTrue(len(Base.create.__doc__) > 0)
        self.assertTrue(len(Base.from_json_string.__doc__) > 0)
        self.assertTrue(len(Base.save_to_file.__doc__) > 0)
        self.assertTrue(len(Base.load_from_file.__doc__) > 0)

    def test_to_json_string(self):
        """ test json """
        r1 = Rectangle(10, 7, 2, 8)
        r1.id = 1
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertTrue(type(json_dictionary) is str)

    def test_json_strto_file(self):
        """ json test """
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r") as my_file:
            read = my_file.read()
            my_list = Base.from_json_string(read)
            self.assertDictEqual(r1.to_dictionary(), my_list[0])

if __name__ == '__main__':
    unittest.main()
