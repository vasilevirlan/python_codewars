import unittest
from exercise import  count_sheep as cs


class TestCountSheep(unittest.TestCase):

    def test1(self):

        ar1 = 3
        outputs = cs(ar1)

        self.assertEqual(outputs,'1 sheep...2 sheep...3 sheep...')


    def test2(self):

        ar1 = 2
        outputs = cs(ar1)

        self.assertEqual(outputs,'1 sheep...2 sheep...')


    def test3(self):

        ar1 = 1
        outputs = cs(ar1)

        self.assertEqual(outputs,'1 sheep...')


if __name__ == '__main__':
    unittest.main()
