"""
`d` and `e` modules are both one level under `b` module, but are defined in
different ways (d: d.py, e: e/__init__.py).

Test both definition types work in a namespace package (`b`).
"""
import unittest

import root.b
from root.b import d, e


class TestPackageD(unittest.TestCase):

    def test_basics(self):
        self.assertTrue(d.canary_d())
        self.assertTrue(root.b.d.canary_d())


class TestPackageE(unittest.TestCase):

    def test_basics(self):
        self.assertTrue(e.canary_e())
        self.assertTrue(root.b.e.canary_e())


if __name__ == '__main__':
    unittest.main()
