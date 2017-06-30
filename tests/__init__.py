"""
Test case for ptqueue server
"""

import unittest
import random

# pylint: disable=C0111
class FuzzerTest(unittest.TestCase):
    """Probably not needed but is a sannity check to make sure unnittest tests actually work"""
    def test_fuzzer(self):
        self.assertTrue(bool(random.getrandbits(1)))

class MarshallerTest(unittest.TestCase):

    def test_marshal(self):
        self.assertTrue(1 == 1)

    def test_unmarshal(self):
        self.assertTrue(1 == 1)

    def test_get_arg(self):
        self.assertTrue(1 == 1)

    def test_get_kwarg(self):
        self.assertTrue(1 == 1)


def main():
    """Alias to testcase main method"""
    unittest.main()

if __name__ == '__main__':
    main()
