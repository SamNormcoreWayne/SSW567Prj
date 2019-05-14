import unittest
import os
from foo.repository import Repository

if __name__ == "__main__":
    test_dir = os.path.join(os.getcwd(), "test")
    discover = unittest.defaultTestLoader.discover(test_dir, 'test_*.py')
    docs_dir = os.path.join(os.getcwd(), "docs")
    report_path = os.path.join(docs_dir, 'test_suite_report.txt')
    a = Repository(filename='sample', dir=os.path.join(docs_dir, 'docs'))
    with open(report_path, 'w') as report:
        report.write(a.output_family())
        runner = unittest.TextTestRunner(stream=report, verbosity=2)
        runner.run(discover)
