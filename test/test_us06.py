import unittest
import os
from foo.repository import Repository

dir = os.path.join(os.getcwd(), "docs")
filename_1 = "sample"

class TestUS06(unittest.TestCase):
    ''' Test Case 06: To test checking eligibility'''
    def test_us06(self):
        rep = Repository(filename_1, dir)
        self.assertNotEqual(rep.check_benefit_eligibility(), "")