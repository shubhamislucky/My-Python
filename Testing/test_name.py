import unittest
from name import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """ Tests for 'name.py'. """

    def test_first_last_name(self):
        formatted_name = get_formatted_name('Shubham', 'Singh')
        self.assertEqual(formatted_name,'Shubham Singh')

    def test_first_middle_last_name(self):
        formatted_name = get_formatted_name('Shubham', 'kumar', 'singh')
        self.assertEqual(formatted_name, 'Shubham Kumar Singh')

unittest.main()
