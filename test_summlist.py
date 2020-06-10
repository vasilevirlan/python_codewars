import unittest
from summ_list import sum_mix as sm

class NamesTestCase(unittest.TestCase):
    """Tests for 'summ_list.py'. Model pentru teste."""

    def test_sum_mix(self):
        """Do  ['1', '1'] work?"""
        result = sm(['1', '1'])
        self.assertEqual(result, 2)

    def test_2(self):
        result1 = sm(['1', '2', '3'])
        self.assertEqual(result1, 6)

unittest.main()
