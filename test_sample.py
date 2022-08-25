import unittest
from unittest.mock import mock_open, patch
from ts3 import clearword
class MyTestCase(unittest.TestCase):
    def test_answer3(self):
        m = mock_open(read_data='qwerty\nddsdsd')
        with patch('builtins.open', m):
            with open('foo') as mock_file:
                file = mock_file.readlines()
                print(file)
                self.assertEqual([clearword(string.strip()) for string in file], [6, 2])