import unittest

import root.b
from root.b import c


class TestPackageC(unittest.TestCase):

    def test_basics(self):
        self.assertTrue(c.canary_c())
        self.assertTrue(root.b.c.canary_c())


if __name__ == '__main__':
    unittest.main()