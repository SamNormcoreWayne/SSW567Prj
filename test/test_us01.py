import unittest
import os
from foo.repository import Repository

dir = os.path.join(os.getcwd(), "docs")
filename = "sample"
repo = Repository(filename, dir)

class TestUS01(unittest.TestCase):
    def test_input_family(self):
        self.assertEqual(len(repo.Family.keys()), True)