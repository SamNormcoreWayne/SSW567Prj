import unittest
import os
from foo.repository import Repository

dir = os.path.join(os.getcwd(), "docs")
filename_1 = "sample"
filename_2 = "test_no_income_larger_30000"

class TestUS03(unittest.TestCase):
    ''' Test Case 03: To test family income beyond $30,000'''
    def test_us03(self):
        rep_1 = Repository(filename_1, dir)
        rep_2 = Repository(filename_2, dir)
        self.assertNotEqual(rep_1.income_more_than_30k(), "US03---> Not family with more than $30,000 income has been found in this file")
        self.assertEqual(rep_2.income_more_than_30k(), "US03---> Not family with more than $30,000 income has been found in this file")
