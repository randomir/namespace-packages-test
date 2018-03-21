import unittest

import root
from root import b


class TestPackageB(unittest.TestCase):

    def test_basics(self):
        self.assertTrue(b.canary_b())
        self.assertTrue(root.b.canary_b())


if __name__ == '__main__':
    unittest.main()