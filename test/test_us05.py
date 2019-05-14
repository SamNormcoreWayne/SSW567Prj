import unittest
import os
from foo.repository import Repository

dir = os.path.join(os.getcwd(), "docs")
filename_1 = "sample"
filename_2 = "test_no_younger_than_5.ged"

class TestUS05(unittest.TestCase):
    ''' Test Case 05: To test children younger than 5'''
    def test_us05(self):
        rep_normal = Repository(filename_1, dir)
        rep_error = Repository(filename_2, dir)
        self.assertEqual(rep_normal.younger_than_5(), True)
        self.assertEqual(rep_error.younger_than_5(), "US05---> Not family with kids younger than 5 years old has been found in this file")

