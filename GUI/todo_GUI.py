'''
First install PySimpleGUI package using -
"pip install PySimpleGUI" command
'''

import PySimpleGUI as pygui
import csv
import datetime
import random
import modules

filename = "todo_list.csv"
fields = ["timestamp", "todo", "status"]

theme = ['Reddit', 'Dark', 'DarkBlue', 'DarkBrown', 'DarkGreen', 'DarkTeal9',
         'DarkPurple', 'DarkRed', 'GreenMono', 'LightGreen', 'Material1', 'Material2',
         'NeutralBlue', 'SandyBeach', 'SystemDefault', 'Tan', 'TealMono']

pygui.theme('TealMono')
print(random.choice(theme))
label = pygui.Text("Type a To-Do : ", font=('Times New Roman', 12))
input_box = pygui.InputText(tooltip="type your todo", key='todo')
add_button = pygui.Button('ADD',
                          button_color=('white', '#4caf50'))
edit_button = pygui.Button('EDIT',
                           button_color=('white', '#2196f3'))
complete_button = pygui.Button('Complete',
                               button_color=('white', '#f44336'))

title = pygui.Text("*********** Your TO-DO **********")
list_title = pygui.Text("My Todo List", font=("Times new roman", 18))

list_box = pygui.Listbox(values=modules.get_todo_list(), key='todos', enable_events=True, size=[70, 10])

header = [
    pygui.Text('To-do', pad=(0, 0), size=(15, 1), justification='c'),
    pygui.Text('Status', pad=(0, 0), size=(30, 1), justification='c'),
]

heading = [header]

# for row in heading:
#     heading.append([
#         pygui.Input(size=(15, 1), pad=(0, 0), key=(row, 0)),
#         pygui.Input(size=(30,1), pad=(0, 0), key=(row, 1)),
#
#     ])
window = pygui.Window("Brain Station 23 TO-DO Application",
                      layout=[[label, input_box, add_button],
                              [list_title],
                              [heading, list_box],
                              [edit_button, complete_button]],
                      resizable=True, size=(700, 400),
                      font=('Times New Roman', 12),
                      element_justification='center',
                      icon='BS_logo_1.ico')
while True:
    event, key = window.read()
    match event:
        case 'ADD':
            modules.write_todo(key['todo'])
            todos = modules.get_todo_list()
            window['todos'].update(values=todos)
        case 'EDIT':
            todo_to_edit = key['todos'][0]
            new_todo = key['todo']
            print("----", todo_to_edit)
            print(">>>>>>>", new_todo)
            todos = modules.get_todo_list()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            modules.edit_todo(todo_to_edit, new_todo)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=key['todos'][0])
        case 'exit':
            print("Program exit, BYE !!")
            break
        case pygui.WIN_CLOSED:
            break

window.close()
