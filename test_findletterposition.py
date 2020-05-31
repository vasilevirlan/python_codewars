import unittest
from find_letter_position import position as ps


class TestLetterPosition(unittest.TestCase):

    def test1(self):

        argm = 'a'
        outputs = ps(argm)

        self.assertEqual(outputs, 'Position of alphabet: 1')

    def test2(self):

        argm = 'z'
        outputs = ps(argm)

        self.assertEqual(outputs, 'Position of alphabet: 26')


if __name__ == '__main__':
    unittest.main()
