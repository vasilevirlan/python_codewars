import unittest
from century_from_year import century as ct

class NameTestCases(unittest.TestCase):

    def test_one(self):
        result = ct(1705)
        self.assertEqual(result, 18)

    def test_two(self):
        result = ct(1900)
        self.assertEqual(result, 19)

    def test_three(self):
        result = ct(1601)
        self.assertEqual(result, 17)

    def test_four(self):
        result = ct(2000)
        self.assertEqual(result, 20)

unittest.main()
