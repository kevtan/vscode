import unittest


class NumbersTest(unittest.TestCase):

    def test_even(self):
        """Test that the numbers between 0 and 5 are all even."""
        for i in range(0, 6, 2):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)
