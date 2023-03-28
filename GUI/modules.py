import csv
import datetime

filename = "todo_list.csv"
fields = ["timestamp", "todo", "status"]


def get_todo_list():
    with open(filename, 'r') as csvData:
        reader = csv.DictReader(csvData)
        data = list(reader)
        list1 = []
        for i, item in enumerate(data):
            list1.append(item['todo'])
    return list1


# def get_todo_list():
#     with open(filename, 'r') as csvData:
#         reader = csv.DictReader(csvData)
#         data = list(reader)
#         list1 = []
#         for item in data:
#             list1.append({"todo": item['todo'], "status": item['status']})
#     return list1


def write_todo(todo):
    try:
        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            rows = list(reader)
    except FileNotFoundError:
        rows = []

    uInput = todo
    # Add user input to list
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    uInput = uInput.title()
    rows.append({"timestamp": timestamp, "todo": uInput, "status": "Undone"})

    # Write list to CSV file
    with open(filename, 'w', newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def edit_todo(todo, new_todo):
    try:
        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            rows = list(reader)
    except FileNotFoundError:
        rows = []

    # print(">>>", rows)
    # Find the todo item with the given ID
    for row in rows:
        if row['todo'] == todo:
            # Update the todo text and timestamp
            row["todo"] = new_todo.title()
            print("-----", row['todo'])
            row["timestamp"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Write the modified rows back to the CSV file
    with open(filename, 'w', newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

# edit_todo('Bowing 727', 'test')
