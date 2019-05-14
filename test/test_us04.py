import unittest
import os
from foo.repository import Repository

dir = os.path.join(os.getcwd(), "docs")
filename_1 = "sample"
filename_2 = "test_no_4_child.ged"

class TestUS04(unittest.TestCase):
    ''' Test Case US04: To test child more than 4'''
    def test_us04(self):
        rep_normal = Repository(filename_1, dir)
        rep_error = Repository(filename_2, dir)
        self.assertEqual(rep_normal.fewer_than_10_kids(), True)
        self.assertEqual(rep_error.fewer_than_10_kids(), "US04---> Not family with more than 10 kids has been found in this file")