import unittest
from shorter_concat import shorter_reverse_longer as sr


class TestShorterReverse(unittest.TestCase):

    def test1(self):
        ar1 = 'one'
        ar2 = 'two'
        output = sr(ar1, ar2)

        self.assertEqual(output, 'twoenotwo')

    def test2(self):
        ar1 = 'three'
        ar2 = 'two'
        output = sr(ar1, ar2)

        self.assertEqual(output, 'twoeerhttwo')

    def test3(self):
        ar1 = 'one'
        ar2 = 'three'
        output = sr(ar1, ar2)

        self.assertEqual(output, 'oneeerhtone')

if __name__ == " __main__":
    unittest.main()
