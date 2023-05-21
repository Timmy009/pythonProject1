import unittest
from OOP.Area import get_area
from OOP.Multiply import multiple
from math import pi


class TestArea(unittest.TestCase):
    def test_area_of_circle_works(self):
        self.assertEquals(get_area(1), pi)
        self.assertAlmostEquals(get_area(0), 0)

    def test_area_function_reject_negative_value(self):
        self.assertRaises(ValueError, get_area, -2)

    def test_that_function_reject_string(self):
        self.assertRaises(TypeError, get_area, "Tas")

    def test_that_mulytiply_works(self):
        self.assertEquals(multiple(2, 4), 8)

    def test_that_mulytiply_reject_negative_works(self):
        self.assertRaises(ValueError,  multiple, -2, -4)

    def test_that_multiple_reject_string(self):
        self.assertRaises(TypeError, multiple, "Tas", 4)