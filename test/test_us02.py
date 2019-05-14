import unittest
import os
from foo.repository import Repository

dir = os.path.join(os.getcwd(), "docs")
filename = "sample"
repo = Repository(filename, dir)


class TestUS02(unittest.TestCase):
    def test_output_family(self):
        self.assertEqual(len(repo.output_family()), True)