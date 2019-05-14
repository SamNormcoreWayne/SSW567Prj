import os
from prettytable import PrettyTable
from foo.readGED import readGED
from foo.family import Family

''' Class Family
    Attributes: (fam_ID, hus, wife, child, income)
    Methods: None
'''

''' Method readGED
    Parameters: (dir, filename)
    Return: generator(dict("fam_ID", "HUSB", "WIFE", "CHIL", "INCOME"))
'''

class Repository():
    def __init__(self, filename, dir=os.getcwd()):
        self.Family = dict()
        self.working_path = dir
        self.filename = filename
        self.input_family()

    def input_family(self):
        path = self.working_path
        filename = self.filename
        fam_lst = list(readGED(path, filename))
        print(fam_lst)
        for fam_dic in fam_lst:
            new_family = Family(fam_dic['fam_ID'], fam_dic['HUSB'], fam_dic["WIFE"], fam_dic["CHIL"], fam_dic["INCOME"])
            self.Family[fam_dic['fam_ID']] = new_family

    def output_family(self):
        field_name = ['ID', 'Hus Name', 'Wife Name', 'Child(ren)', 'Income']
        table = PrettyTable(field_names=field_name)
        for family in self.Family.values():
            table.add_row([family.fam_ID, family.hus, family.wife, family.child, family.income])
        
        print("Families")
        print(table.get_string(sortby='ID'))