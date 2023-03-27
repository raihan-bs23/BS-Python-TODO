import glob
myfiles = glob.glob("EXP/TEST/*.txt")
for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read().upper())


# print(myfiles)