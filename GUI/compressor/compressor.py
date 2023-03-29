import PySimpleGUI as gui
from zip_creator import make_archive



label1 = gui.Text("Select multiple files to compress : ")
input1 = gui.Input()
button1 = gui.FilesBrowse("Choose", key='files')

label2 = gui.Text("Select Destination path to store  : ")
input2 = gui.Input()
button2 = gui.FolderBrowse("Select", key='destination')

button3 = gui.Button("Compress")
output_label = gui.Text(key='output')
window = gui.Window("File Compressor", layout=[[label1, input1, button1],
                                               [label2, input2, button2],
                                               [button3, output_label]])

while True:
    event, values = window.read()
    print(event)
    print(values)
    filepaths = values['files'].split(';')
    folder = values['destination']
    make_archive(filepaths, folder)
    window['output'].update(value="Compression Complete !", text_color='red')

window.close()
