import os
from foo.repository import Repository

''' Class Repository
    Attribute: (dict(Family), working_path, filename)
    Methods: (input_family(), output_family())
'''

def main():
    dir = os.path.join(os.getcwd(), "docs")
    filename = "sample"
    repo = Repository(filename, dir)
    repo.output_family()

if __name__ == "__main__":
    main()