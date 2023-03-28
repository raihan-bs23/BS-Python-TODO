import csv

filename = "todo_list.csv"
fields = ["timestamp", "todo", "status"]


def get_todo_list():
    list1 = []
    print("************* TO DO List ***********\n")
    with open(filename, 'r') as csvData:
        reader = csv.DictReader(csvData)
        rows = list(reader)
        for i, item in enumerate(rows):
            list1.append(item)
            return list1
        #     print(f"{i + 1}- {item['todo']}")

