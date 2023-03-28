import PySimpleGUI as gui

label1 = gui.Text("Select multiple files to compress : ")
input1 = gui.Input()
button1 = gui.FileBrowse("Choose")

label2 = gui.Text("Select Destination path to store  : ")
input2 = gui.Input()
button2 = gui.FolderBrowse("Select")

button3 = gui.Button("Compress")

window = gui.Window("File Compressor", layout=[[label1, input1, button1],
                                               [label2, input2, button2],[button3]])
window.read()
window.close()
help(gui)