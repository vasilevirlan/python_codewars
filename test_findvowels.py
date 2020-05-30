import unittest
from find_vowels_index import vowels_index as vi


class TestVowelsIndex(unittest.TestCase):

    def test_vi(self):

        argm = 'vasile'
        outputs = vi(argm)

        self.assertEqual(outputs, [2, 4, 6])

    def test_vi2(self):

        argm = 'Python'
        outputs = vi(argm)

        self.assertEqual(outputs, [2, 5])

    def test_vi3(self):

        argm = 'software'
        outputs = vi(argm)

        self.assertEqual(outputs, [2, 6, 8])

    def test_vi4(self):

        argm = 'vvvvv'
        outputs = vi(argm)

        self.assertEqual(outputs, [])

    def test_vi5(self):

        argm = 'file'
        outputs = vi(argm)

        self.assertEqual(outputs, [2, 4])


if __name__ == '__main__':
    unittest.main()
