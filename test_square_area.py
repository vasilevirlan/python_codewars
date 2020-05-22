import unittest
from square_area import square_area as sq


class TestSquareArea(unittest.TestCase):

    def test1(self):

        argm1 = 2
        outputs = sq(argm1)

        self.assertEqual(outputs, 1.62)

    def test2(self):

        argm1 = 0
        outputs = sq(argm1)

        self.assertEqual(outputs, 0)

    def test3(self):

        argm1 = 14.05
        outputs = sq(argm1)

        self.assertEqual(outputs, 80)

    def test4(self):

        argm1 = 1
        outputs = sq(argm1)

        self.assertEqual(outputs, 0.41)

    def test4(self):

        argm1 = 100
        outputs = sq(argm1)

        self.assertEqual(outputs, 4052.85)

    def test5(self):

        argm1 = 10
        outputs = sq(argm1)

        self.assertEqual(outputs, 40.53)


if __name__ == '__main__':
    unittest.main()
