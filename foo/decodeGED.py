import os

tag = ['HUSB', 'WIFE', 'CHIL', 'AGE', 'INCOME']
tag_2 = ['AGE']

def to_str(lst):
    s = ""
    for item in lst:
        s += item
    return s

def line_process(lst):
    tmp = lst
    if tmp[0] == '0':
        if tmp[2].isupper():
            tmp[1], tmp[2] = tmp[2], tmp[1]
            if tmp[1] == 'FAM':
                tmp[1] = "|{}|Y|".format(tmp[1])
                
    else:
        if tmp[1] in tag:
            tmp[1] = "|{}|Y|".format(tmp[1])
        else:
            tmp[1] = "|{}|N|".format(tmp[1])
    return tmp



def decodeGED(dir, filename):
    path = os.path.join(dir, filename)
    try:
        fp = open(path + '.ged', 'r')
    except FileNotFoundError as fe:
        raise(fe)
    fp2 = open("{}_ged.out".format(path), 'w+')
    for line in fp:
        line = line.rstrip(' \n')
        line_lst = line.split(' ', 2)
        line_str = to_str(line_process(line_lst))
        fp2.write(line_str + '\n')
    fp.close()
    fp2.close()

def main():
    dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    decodeGED(os.path.join(dir, "docs"), "sample")

if __name__ == "__main__":
    main()