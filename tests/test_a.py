import unittest

import root
from root import a


class TestPackageA(unittest.TestCase):

    def test_basics(self):
        self.assertTrue(a.canary_a())
        self.assertTrue(root.a.canary_a())


if __name__ == '__main__':
    unittest.main()