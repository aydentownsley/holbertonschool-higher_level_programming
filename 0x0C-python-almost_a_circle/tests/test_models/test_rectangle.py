#!/usr/bin/python3
""" Test Module for Rectangle Class """


import unittest
import json
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Tests attr values and exceptions of Rectangle class """

    @classmethod
    def setUpClass(cls):
        """ sets up instances for tests """
        cls.r1 = Rectangle(5, 1, id=50)
        cls.r2 = Rectangle(3, 5, id=45)
        cls.r3 = Rectangle(2, 8)
        cls.r4 = Rectangle(4, 2, 8)
        cls.r5 = Rectangle(2, 4, 2, 8)
        cls.r6 = Rectangle(1, 2, 4, 2, 8)

    @classmethod
    def tearDownClass(cls):
        """ dels instances at end """
        del cls.r1
        del cls.r2
        del cls.r3
        del cls.r4
        del cls.r5
        del cls.r6

    def test_attrs(self):
        """ tests id, w, h, x, y, set, get """
        # id tests
        self.assertEqual(self.r1.id, 50)
        self.assertEqual(self.r2.id, 45)
        self.assertEqual(self.r6.id, 8)
        # width tests
        self.assertEqual(self.r1.width, 5)
        self.assertEqual(self.r6.width, 1)
        # height test
        self.assertEqual(self.r2.height, 5)
        self.assertEqual(self.r4.height, 2)
        # x pos test
        self.assertEqual(self.r3.x, 0)
        self.assertEqual(self.r4.x, 8)
        self.assertEqual(self.r6.x, 4)
        # y pos test
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r5.y, 8)

    def test_excpets(self):
        """ tests the exceptions in validating """
        with self.assertRaises(TypeError):
                                Rectangle("Width", 5)
        with self.assertRaises(TypeError):
                                Rectangle(5, "Height")
        with self.assertRaises(TypeError):
                                Rectangle(5, 5, "x")
        with self.assertRaises(TypeError):
                                Rectangle(5, 5, 5, "y")
        with self.assertRaises(ValueError):
                                Rectangle(-5, 5)
        with self.assertRaises(ValueError):
                                Rectangle(5, -5)
        with self.assertRaises(ValueError):
                                Rectangle(5, 5, -5)
        with self.assertRaises(ValueError):
                                Rectangle(5, 5, 5, -5)
