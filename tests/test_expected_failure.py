import unittest


class ExpectedFailureTestCase(unittest.TestCase):
    @unittest.expectedFailure
    def test_fail(self):
        """This test is supposed to fail so you can see what a failed test looks like!"""
        self.assertEqual(1, 0, "broken")
