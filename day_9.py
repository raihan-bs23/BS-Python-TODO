import csv
import datetime
# Define CSV file name and column names
filename = "todo_list.csv"
fields = ["timestamp", "todo"]
todo = []
'''
This program is to solve a daily to do manager using python language
'''
while True:
    userAction = input("Type add, show, edit, complete or exit -")
    userAction = userAction.strip().lower()
    # strip for removing all the whitespace and lower for convert all the char to lowercase
    if userAction.startswith('add'):
        # Read existing CSV file (if it exists) and append new input
        try:
            with open(filename, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                rows = list(reader)
        except FileNotFoundError:
            rows = []

        uInput = userAction[4:]
        # Add user input to list
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        uInput = uInput.title()
        rows.append({"timestamp": timestamp, "todo": uInput})

        # Write list to CSV file
        with open(filename, 'w', newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)
    elif userAction.startswith("show"):
        print("************* TO DO List ***********\n")
        with open(filename, 'r') as csvData:
            reader = csv.DictReader(csvData)
            rows = list(reader)
            for i, item in enumerate(rows):
                print(f"{i+1}- {item['todo']}")

    elif userAction.startswith("edit"):
        try:
            with open(filename, 'r') as csvData:
                reader = csv.DictReader(csvData)
                rows = list(reader)
                index = int(userAction[5:].strip())
                print(rows[index - 1]["todo"])
                uInput = input(f"Enter new Todo_{index} - ")
                uInput = uInput.title()
                rows[index - 1]["todo"] = uInput
                # Write updated rows to CSV file
                with open(filename, 'w', newline="") as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=fields)
                    writer.writeheader()
                    writer.writerows(rows)
        except ValueError:
            print("You have entered a wrong command !!")
            continue
    elif userAction.startswith('complete'):
        try:
            with open(filename, 'r') as csvData:
                reader = csv.DictReader(csvData)
                rows = list(reader)
                index = int(userAction[9:])
                rows.pop(index-1)
                # Write updated rows to CSV file
                with open(filename, 'w', newline="") as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=fields)
                    writer.writeheader()
                    writer.writerows(rows)
        except ValueError:
            print("you have entered a wrong command !!")
            continue
        except IndexError:
            print("There's no such a Index !!")
    elif userAction.startswith('exit'):
        break
    else:
        print("You have enter unknown command !!")
print("Program exit. Bye !")
