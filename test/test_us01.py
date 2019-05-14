import unittest
import os
from foo.repository import Repository

dir = os.path.join(os.getcwd(), "docs")
filename = "sample"


class TestUS01(unittest.TestCase):
    def test_input_family(self):
        repo = Repository(filename, dir)
        self.assertEqual(len(repo.Family.keys()), True)
        with self.assertRaises(FileNotFoundError):
            repo_error = Repository("nothing", dir)
