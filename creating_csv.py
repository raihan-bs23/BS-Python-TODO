import csv
import shutil
import webbrowser

with open("EXP/Files/demo.csv", 'r') as file:
    data = list(csv.reader(file))

id = input("Enter You BS ID-")


for i in data[1:]:
    if i[0] == id:
        print(i[1:])

'''
to maipulate zip file
'''
# shutil.make_archive("Output", "zip", "EXP/TEST")
# print("Zip File created!!")

'''
search from website and make scrawler 
'''
user_input = input("Enter your keyword - ")
webbrowser.open("https://www.google.com/search?q="+ user_input)