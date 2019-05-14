import os
from prettytable import PrettyTable
from collections import defaultdict
from foo.readGED import readGED
from foo.family import Family
from foo.decodeGED import decodeGED

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

    #us_01 Read .ged file
    def input_family(self):
        path = self.working_path
        filename = self.filename
        decodeGED(path, filename)
        fam_lst = list(readGED(path, filename))
        print(fam_lst)
        for fam_dic in fam_lst:
            new_family = Family(fam_dic['fam_ID'], fam_dic['HUSB'], fam_dic["WIFE"], fam_dic["CHIL"], fam_dic["INCOME"])
            self.Family[fam_dic['fam_ID']] = new_family

    #us_02 Family summary
    def output_family(self):
        field_name = ['ID', 'Hus Name', 'Wife Name', 'Child(ren)', 'Income']
        table = PrettyTable(field_names=field_name)
        if list(self.Family.values()) == []:
            return False
        for family in self.Family.values():
            table.add_row([family.fam_ID, family.hus, family.wife, family.child, family.income])

        print("Families")
        print(table.get_string(sortby='ID'))
        return table.get_string()

    
    #us_03 Income more than $30,000
    def income_more_than_30k(self):
        """Check and list out all families with household income more than $30,000"""
        result = dict()

        for fam in self.Family.values():
            if int(fam.income) > 30000:
                result[fam.fam_ID] = fam.income
        
        if not result:
            print('\n')
            return "US03---> Not family with more than $30,000 income has been found in this file"
        
        else:
            field_name = ['ID', 'Income']
            table = PrettyTable(field_names = field_name)
            for ID, income in result.items():
                table.add_row([ID, income])
            print('\n', 'Families with income more than $30,000. \n')
            print(table)
            return True

    #us_04 Fewer than 10 kids
    def fewer_than_10_kids(self):
        """Check if there is family with more than 10 kids"""
        result = dict()

        for fam in self.Family.values():
            if len(fam.child.keys()) > 10:
                result[fam.fam_ID] = [i for i in fam.child.keys()]
        
        if not result:
            print('\n')
            return "US04---> Not family with more than 10 kids has been found in this file"

        else:
            field_name = ['ID', 'Number of kids', 'Names']
            table = PrettyTable(field_names = field_name)
            for ID, kids in result.items():
                table.add_row([ID, len(kids), kids])

            print('\n', 'Families with more than 10 kids')
            print(table)
            return True


    #us_05 Younger than 5
    def younger_than_5(self):
        """Check and list out families with kids younger than 5 years old"""
        result = defaultdict(dict)    

        for fam in self.Family.values():
            for kid, age in fam.child.items():
                if int(age) < 5:
                    result[fam.fam_ID][kid] = age
        
        if not result:
            print('\n')
            return "US05---> Not family with kids younger than 5 years old has been found in this file"

        else:
            field_name = ['ID', 'Names', 'Age']
            table = PrettyTable(field_names = field_name)
            for key, value in result.items():
                for kid, age in value.items():
                    table.add_row([key, kid, age])
                    

            print('\n', 'Families with kids younger than 5 years old')
            print(table)
            return True

    
    #us_06 Check benefit eligibility
    def check_benefit_eligibility(self):
        """Check for each family's benefit eligibility"""
        result = dict()

        for fam in self.Family.values():
            if int(fam.income) > 30000:
                result[fam.fam_ID] = 'Not eligible for benefit' #household income > 30,000
            
            elif fam.hus == 'N/A' or fam.wife == 'N/A': #single parent families
                for age in fam.child.values():
                    if int(age) >= 18:
                        result[fam.fam_ID] = "Eligible for $1500 per month benefit" #at least one kid age >= 18

                else:
                    if len(fam.child.keys()) >= 3:
                        result[fam.fam_ID] = "Eligible for $2500 per month benefit" #all kids below age 18 and >= 3 kids
                
                    else:
                        result[fam.fam_ID] = "Eligible for $2000 per month benefit" #all kids below age 18 but < 3 kids
            
            else:   #double-parent families
                for age in fam.child.values():
                    if int(age) >= 18:
                        result[fam.fam_ID] = "Eligible for $1000 per month benefit" #at leaset one kid age >= 18

                else:
                    if len(fam.child.keys()) >= 3:
                        result[fam.fam_ID] = "Eligible for $2000 per month benefit" #all kids below age 18 and >= 3 kids
                
                    else:
                        result[fam.fam_ID] = "Eligible for $1500 per month benefit" #all kids below age 18 but < 3 kids

        
        field_name = ['ID', 'Benefit eligibility']
        table = PrettyTable(field_names = field_name)
        for key, value in result.items():
            table.add_row([key, value])

        print('\n', 'Benefit eligibility summary')
        print(table)
        return table.get_string()