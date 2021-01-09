import unittest

class TestMaxInteger(unittest.TestCase):
    """ Unit Test for Max Int """

    def test_max(self):
        """ tests valid input """

        self.assertEqual(max_integer([1, 2, 4, 8, 16]), 16)
        self.assertEqual(max_integer([2, -6, 0, -99, 32]), 32)
        self.assertEqual(max_integer([-13, -4, -5, 0, -12]), 0)
        self.assertEqual(max_integer([-300]), -300)
        self.assertEqual(max_integer([], None)

    def test_type(self):
        """ test type input """

        self.assertRaises(TypeError, max_integer(), ["toast", "brush", "can", "sing"])
        self.assertRaises(TypeError, max_integer(), [0.0, 4.3, 9.0])
