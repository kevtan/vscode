import random
import sys
import unittest

import numpy as np


class MyTestCase(unittest.TestCase):
    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(np.__version__ < "1.20", "numpy version too old")
    def test_format(self):
        # tests that only work for a certain version of the library
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows OS")
    def test_windows_support(self):
        # windows specific testing code
        pass

    def test_maybe_skipped(self):
        if random.random() > 0.5:
            self.skipTest("external resource not available")


@unittest.skip("demonstrate test case skipping")
class MySkippedTestCase(unittest.TestCase):
    def test_not_run(self):
        pass
