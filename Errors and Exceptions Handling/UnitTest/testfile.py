import unittest

import file

class TestClass(unittest.TestCase):

    def test_first(self):
        string = 'Jitender'
        result = file.upper(string)
        self.assertEqual(result,'JITENDER')

    def test_multiple_words(self):
        string = 'Python is the coolest programming language'
        result = file.upper(string)
        self.assertEqual(result,'PYTHON IS THE COOLEST PROGRAMMING LANGUAGE')

    def test_cap_all_word(self):
        string = 'Python language'
        result = file.capit_all_words(string)
        self.assertEqual(result, 'Python Language')

    def test_capitalize_only_first(self):
        string = 'Python is the coolest programming language'
        result = file.capit(string)
        self.assertEqual(result, 'Python is the coolest programming language')


if __name__ == '__main__':
    unittest.main()