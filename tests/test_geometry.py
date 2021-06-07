# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from gistools.geometry import *

class TestSimple(unittest.TestCase):

    def test_angle(self):
        func = angle
        args = Point(0, 0), Point(1, 1), Point(1, 0)
        kwargs = dict()
        answer = 45
        self.assertEqual(func(*args, **kwargs), answer)

    def test_extrapolate(self):
        func = extrapolate
        args = Point(0, 0), Point(1, 1)
        kwargs = dict(ratio=2)
        answer = Point(2, 2)
        self.assertEqual(func(*args, **kwargs), answer)

    def test_which_side(self):
        args = Point(0, 0), Point(1, 1), Point(0, 1)
        kwargs = dict()
        answer = 'left'
        self.assertEqual(func(*args, **kwargs), answer)

    def test_which_side_line(self):
        func = which_side_line
        # Subtest: 'right'
        args = LineString([(0, 0), (1, 1)]), Point(1, 0)
        kwargs = dict()
        answer = 'right'
        self.assertEqual(func(*args, **kwargs), answer)
        # Subtest: 'left'
        args = LineString([(0, 0), (1, 1)]), Point(0, 1)
        kwargs = dict()
        answer = 'left'
        self.assertEqual(func(*args, **kwargs), answer)

if __name__ == '__main__':
    unittest.main()
    print('OK!')