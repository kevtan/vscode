import importlib
import unittest

import my_sum


class TestMySum(unittest.TestCase):

    def test_my_sum(self):
        self.assertEqual(my_sum.sum([1, 2, 3]), 6)
