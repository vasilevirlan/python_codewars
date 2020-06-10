import unittest
from find_vowels import vowels_indices as vi


class NameTestCases(unittest.TestCase):

    def test_one(self):
        result = vi('Mmmm')
        self.assertEqual(result, [])

    def test_two(self):
        result = vi('Super')
        self.assertEqual(result, [2, 4])

    def test_three(self):
        result = vi('Apple')
        self.assertEqual(result, [1, 5])

    def test_four(self):
        result = vi('YoMama')
        self.assertEqual(result, [1, 2, 4, 6])


unittest.main()
