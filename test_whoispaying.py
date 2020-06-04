import unittest
from who_is_paying import who_is_paying as wh


class TestWhoIsPaying(unittest.TestCase):

    def test1(self):

        ar1 ='Vasile'
        outputs = wh(ar1)

        self.assertEqual(outputs, ['Vasile', 'Va'])

    def test2(self):

        ar1 ='Va'
        outputs = wh(ar1)

        self.assertEqual(outputs, ['Va'])

    def test3(self):

        ar1 =''
        outputs = wh(ar1)

        self.assertEqual(outputs, [''])


if __name__ == '__main__':
    unittest.main()
