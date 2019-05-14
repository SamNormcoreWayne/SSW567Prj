import os
from foo.decodeGED import decodeGED
from foo.repository import Repository

''' Class Repository
    Attribute: (dict(Family), working_path, filename)
    Methods: (input_family(), output_family())
'''


def main():
    dir = os.path.join(os.getcwd(), "docs")
    filename = "sample"
    decodeGED(dir, filename)
    repo = Repository(filename, dir)
    repo.output_family()
    print(repo.income_more_than_30k())
    repo.fewer_than_10_kids()
    repo.younger_than_5()
    repo.check_benefit_eligibility()

if __name__ == "__main__":
    main()