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
    match userAction:
        case 'add':
            # Read existing CSV file (if it exists) and append new input
            try:
                with open(filename, 'r') as csvfile:
                    reader = csv.DictReader(csvfile)
                    rows = list(reader)
            except FileNotFoundError:
                rows = []

            uInput = input("Enter a Todo - ")
            # Add user input to list
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            uInput = uInput.title()
            rows.append({"timestamp": timestamp, "todo": uInput})

            # Write list to CSV file
            with open(filename, 'w', newline="") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fields)
                writer.writeheader()
                writer.writerows(rows)
        case 'show':
            print("************* TO DO List ***********\n")
            with open(filename, 'r') as csvData:
                reader = csv.DictReader(csvData)
                rows = list(reader)
                for i, item in enumerate(rows):
                    print(f"{i+1}- {item['todo']}")

        case 'edit':
            with open(filename, 'r') as csvData:
                reader = csv.DictReader(csvData)
                rows = list(reader)
                index = int(input("Enter the number of the todo to Edit(i.e. 1) - "))
                print(rows[index - 1]["todo"])
                uInput = input(f"Enter new Todo_{index} - ")
                uInput = uInput.title()
                rows[index - 1]["todo"] = uInput
                # Write updated rows to CSV file
                with open(filename, 'w', newline="") as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=fields)
                    writer.writeheader()
                    writer.writerows(rows)
        case 'complete':
            with open(filename, 'r') as csvData:
                reader = csv.DictReader(csvData)
                rows = list(reader)
                index = int(input("Enter the number of the todo you have completed (i.e. 1) - "))
                rows.pop(index-1)
                # Write updated rows to CSV file
                with open(filename, 'w', newline="") as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=fields)
                    writer.writeheader()
                    writer.writerows(rows)
        case 'exit':
            break
        case whatever:
            print("You have entered unknown command !!")
print("Program exit. Bye !")
