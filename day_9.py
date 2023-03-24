import csv
import datetime
# Define CSV file name and column names
filename = "todo_list.csv"
fields = ["timestamp", "todo"]
todo = []


while True:
    userAction = input("Type add, show, edit, complete or exit -")
    userAction = userAction.strip().lower()
    # strip for removing all the whitespace and lower for convert all the char to lowercase
    if 'add' in userAction:
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
    elif 'show' in userAction:
        print("************* TO DO List ***********\n")
        with open(filename, 'r') as csvData:
            reader = csv.DictReader(csvData)
            rows = list(reader)
            for i, item in enumerate(rows):
                print(f"{i+1}- {item['todo']}")

    elif 'edit' in userAction:
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
    elif 'complete' in userAction:
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
    elif 'exit' in userAction:
        break
    else:
        print("You have enter unknown command !!")
print("Program exit. Bye !")
