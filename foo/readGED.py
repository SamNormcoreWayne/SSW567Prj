import os

tag = ['HUSB', 'WIFE', 'CHIL', 'AGE', 'INCOME']
tag_2 = ['AGE']

def readGED(dir, filename):
    path = os.path.join(dir, filename + '_ged.out')
    fam_ID = 'N/A'
    dic = dict()
    with open(path, 'r') as fp:
        for line in fp:
            if line == '\n':
                break
            line = line.rstrip('\n')
            if line.startswith("0|FAM|Y"):

                hus_name = 'N/A'
                wife_name = 'N/A'
                child = dict()
                child_name = ""
                name_count = 1
                income = "N/A"
                tmp = line.split('|')
                fam_ID = tmp.pop()

            if line.startswith("1|HUSB|Y|"):
                hus_name = line.split('|').pop()
            if line.startswith("1|WIFE|Y|"):
                wife_name = line.split('|').pop()
            if line.startswith("1|CHIL|Y"):
                child_name = line.split('|').pop()
                while child_name in child:
                    child_name += "_{}".format(str(name_count))
                child[child_name] = ""
            if line.startswith("2|AGE|Y|"):
                child[child_name] = line.split("|").pop()
            if line.startswith("1|INCOME|Y|"):
                income = line.split("|").pop()
                if income == "":
                    income = "None"
            if income != "N/A":
                dic = {"fam_ID": fam_ID, "HUSB": hus_name, "WIFE": wife_name, "CHIL": child, "INCOME": income}
                yield dic
