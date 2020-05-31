import unittest
from power_2 import powers_of_two as pw2


class TestPowerTwo(unittest.TestCase):

    def test1(self):

        argm1 = 0
        outputs = pw2(argm1)

        self.assertEqual(outputs, [1])

    def test2(self):

        argm1 = 1
        outputs = pw2(argm1)

        self.assertEqual(outputs, [1, 2])

    def test3(self):

        argm1 = 2
        outputs = pw2(argm1)

        self.assertEqual(outputs, [1, 2, 4])

    def test4(self):

        argm1 = 4
        outputs = pw2(argm1)

        self.assertEqual(outputs, [1, 2, 4, 8, 16])

    def test_bad_type(self):
        argm = 'string'
        with self.assertRaises(TypeError):
            result = pw2(argm)


if __name__ == '__main__':
    unittest.main()
