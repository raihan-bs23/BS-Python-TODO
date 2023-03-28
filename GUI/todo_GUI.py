'''
First install PySimpleGUI package using -
"pip install PySimpleGUI" command
'''

import PySimpleGUI as pygui
import csv
import datetime


filename = "todo_list.csv"
fields = ["timestamp", "todo", "status"]

pygui.theme('LightBlue')
label = pygui.Text("Type a to-do : ", font=('Times New Roman', 12))
input_box = pygui.InputText(tooltip="type your todo", key='todo')
add_button = pygui.Button("ADD")
edit_button = pygui.Button("EDIT")
title = pygui.Text("*********** Your TO-DO **********")
with open(filename, 'r') as csvData:
    reader = csv.DictReader(csvData)
    rows = list(reader)
    for i, item in enumerate(rows):
        print(f"{i + 1}- {item['todo']}")
        list_box = pygui.Listbox(values=item['todo'], key='todos', enable_events=True, size=[45, 10])

window = pygui.Window("BS TO-DO App",
                      layout= [[label], [input_box], [add_button],
                               [title],
                               [list_box, edit_button]],
                      resizable=True, size=(400, 150),
                      font=('Times New Roman', 12),
                      element_justification='center',
                      icon='BS_logo.ico')
while True:
    event, key = window.read()
    print(event)
    print(key['todo'])
    match event:
        case 'ADD':
            try:
                with open(filename, 'r') as csvfile:
                    reader = csv.DictReader(csvfile)
                    rows = list(reader)
            except FileNotFoundError:
                rows = []

            uInput = key['todo']
            # Add user input to list
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            uInput = uInput.title()
            rows.append({"timestamp": timestamp, "todo": uInput, "status": "Undone"})

            # Write list to CSV file
            with open(filename, 'w', newline="") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fields)
                writer.writeheader()
                writer.writerows(rows)
        case 'exit':
            print("Program exit, BYE !!")
            break
        case pygui.WIN_CLOSED:
            break


window.close()

