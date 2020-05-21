import unittest
from merge_sorted_list import merge_lists as ms


class TestMergeSortedList(unittest.TestCase):

    def test_ms(self):

        argm1 = [1, 3, 5]
        argm2 = [2, 4, 6]
        outputs = ms(argm1, argm2)

        self.assertEqual(outputs, [1, 2, 3, 4, 5, 6])

    def test_ms_2(self):

        argm1 = [2, 4, 8]
        argm2 = [2, 4, 6]
        output1 = ms(argm1, argm2)

        self.assertEqual(output1, [2, 4, 6, 8])

    def test_ms_3(self):

        argm1 = []
        argm2 = []
        output1 = ms(argm1, argm2)

        self.assertEqual(output1, [])

    def test_ms_4(self):

        argm1 = []
        argm2 = [6, 0, 2, 4]
        output1 = ms(argm1, argm2)

        self.assertEqual(output1, [0, 2, 4, 6])


if __name__ == '__main__':
    unittest.main()
