#!/usr/bin/python3
""" Test Module for Square Class """

import unittest
import json
from models.square import Square


class TestRectangle(unittest.TestCase):
    """ Tests attr values and exceptions of Square class """

    @classmethod
    def setUpClass(cls):
        """ sets up instances for tests """
        cls.s1 = Square(5)
        cls.s2 = Square(3)
        cls.s3 = Square(2, 8)
        cls.s4 = Square(4, 2, 8)
        cls.s5 = Square(2, 4, 2, 8)

    @classmethod
    def tearDownClass(cls):
        """ dels instances at end """
        del cls.s1
        del cls.s2
        del cls.s3
        del cls.s4
        del cls.s5

    def test_attrs(self):
        """ tests id, size, x, y, set, get """
        # id tests
        self.assertEqual(self.s1.id, 6)
        self.assertEqual(self.s2.id, 7)
        self.assertEqual(self.s5.id, 8)
        # size tests
        self.assertEqual(self.s1.size, 5)
        self.assertEqual(self.s5.size, 2)
        # x pos test
        self.assertEqual(self.s3.x, 8)
        self.assertEqual(self.s4.x, 2)
        self.assertEqual(self.s5.x, 4)
        # y pos test
        self.assertEqual(self.s4.y, 8)
        self.assertEqual(self.s5.y, 2)

    def test_excepts(self):
        """ tests the exceptions in validating """
        with self.assertRaises(TypeError):
                                Square("Size")
        with self.assertRaises(TypeError):
                                Square(5, "x")
        with self.assertRaises(TypeError):
                                Square(5, 5, "y")
        with self.assertRaises(ValueError):
                                Square(-5, 5)
        with self.assertRaises(ValueError):
                                Square(5, -5)
        with self.assertRaises(ValueError):
                                Square(5, 5, -5)
