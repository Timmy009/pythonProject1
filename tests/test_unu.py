import unittest
from morning_code.Take_in import ret


class TestArea(unittest.TestCase):

    def test_area_of_circle_works(self):
        self.assertEquals(ret(1.6, 1.5), 3.1)

    def test_that_function_reject_string(self):
        self.assertRaises(TypeError, ret, 3, 5)