import unittest
from divisible_by import divisible_by as div


class TestDivisible(unittest.TestCase):

    def test_1(self):

        """Test for divisible_by.py."""

        numbers = [1, 2, 3, 4, 5, 6]
        divisor = 2
        result = div(numbers, divisor)

        numbers = [1, 2, 3, 4, 5, 6]
        divisor = 3
        result1 = div(numbers, divisor)

        self.assertEqual(result, [2, 4, 6])
        self.assertEqual(result1, [3, 6])


if __name__ == '__main__':
    unittest.main()
