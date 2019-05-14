import random
import names

log_file = 'sample.ged'

try:
    fp = open(log_file, 'w')
except FileExistsError:
    print(f"Can't open {log_file}")

else:
    with fp:
        # Generate double-parent families
        for i in range(1, 4):
            fp.write(f"0 @F{i}@ FAM \n")
            lastname = names.get_last_name()
            fp.write(f"1 HUSB {names.get_first_name(gender = 'male')} {lastname} \n")
            fp.write(f"1 WIFE {names.get_full_name(gender = 'female')} \n")
            num = random.randint(1, 5)
            for i in range(num):
                fp.write(f"1 CHIL {names.get_first_name()} {lastname} \n")
                fp.write(f"2 AGE {random.randint(1, 25)} \n")
            fp.write(f"1 INCOME {random.randint(200, 700) * 100} \n")


        #Generate single-parent families with father
        for i in range(4, 8):
            fp.write(f"0 @F{i}@ FAM \n")
            lastname = names.get_last_name()
            fp.write(f"1 HUSB {names.get_first_name(gender = 'male')} {lastname} \n")
            num = random.randint(1, 5)
            for i in range(num):
                fp.write(f"1 CHIL {names.get_first_name()} {lastname} \n")
                fp.write(f"2 AGE {random.randint(1, 25)} \n")
            fp.write(f"1 INCOME {random.randint(200, 700) * 100} \n")


        #Generate single-parent families with mother
        for i in range(8, 11):
            fp.write(f"0 @F{i}@ FAM \n")
            lastname = names.get_last_name()
            fp.write(f"1 WIFE {names.get_full_name(gender = 'female')} \n")
            num = random.randint(1, 5)
            for i in range(num):
                fp.write(f"1 CHIL {names.get_first_name()} {lastname} \n")
                fp.write(f"2 AGE {random.randint(1, 25)} \n")
            fp.write(f"1 INCOME {random.randint(200, 700) * 100} \n")

