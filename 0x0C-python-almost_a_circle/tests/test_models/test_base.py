#!/usr/bin/python3
"""
Base Testing Module
-------
This module will test
different cases of the
Base class to make sure
the output matches expected
outputs
"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ tests results of the base class """

    @classmethod
    def setUpClass(cls):
        """ set ups test cases """
        cls.b1 = Base()
        cls.b2 = Base(365)
        cls.b3 = Base(0)
        cls.b4 = Base(-10)
        cls.b5 = Base()

    @classmethod
    def tearDownClass(cls):
        """ deletes instances at end """
        del cls.b1
        del cls.b2
        del cls.b3
        del cls.b4
        del cls.b5

    def test_arguments(self):
        """ wrong argument number """
        self.assertRaises(Exception, Base.__init__, 1, 5)

    def test_init(self):
        """ tests init functions """
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 365)
        self.assertEqual(self.b3.id, 0)
        self.assertEqual(self.b4.id, -10)
        self.assertEqual(self.b5.id, 2)
        self.assertEqual(self.b1._Base__nb_objects, 2)
