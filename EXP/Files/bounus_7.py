filenames = ["1.log", "2.activate", "3.test_demo"]

for filename in filenames:
    filenames = filename.replace('.', '-') + ".txt"
    print(filenames)