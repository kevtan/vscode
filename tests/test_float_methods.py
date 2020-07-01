import unittest
import math


class TestFloatMethods(unittest.TestCase):
    def test_as_integer_ratio1(self):
        self.assertEqual((10.0).as_integer_ratio(), (10, 1))

    def test_as_integer_ratio2(self):
        with self.assertRaises(OverflowError):
            math.inf.as_integer_ratio()

    def test_as_integer_ratio3(self):
        with self.assertRaises(ValueError):
            math.nan.as_integer_ratio()
