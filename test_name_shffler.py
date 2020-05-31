import unittest
from name_shuffler import name_shuffler as ns


class TestNameShuffler(unittest.TestCase):

    def test1(self):

        argm1 = 'Vasile Virlan'
        outputs = ns(argm1)

        self.assertEqual(outputs, 'Virlan Vasile')

    def test2(self):

        argm1 = ''
        outputs = ns(argm1)

        self.assertEqual(outputs, '')

    def test3(self):

        argm1 = 'Vasile'
        outputs = ns(argm1)

        self.assertEqual(outputs, 'Vasile')


if __name__ == '__main__':
    unittest.main()
