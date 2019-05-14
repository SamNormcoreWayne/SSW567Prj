import unittest
import os
from foo.repository import Repository

dir = os.path.join(os.getcwd(), "docs")
filename = "sample"


class TestUS01(unittest.TestCase):
    ''' Test Case 01: To test read ged files'''
    def test_input_family(self):
        repo = Repository(filename, dir)
        self.assertNotEqual(len(repo.Family.keys()), 0)
        with self.assertRaises(FileNotFoundError):
            Repository("nothing", dir)
