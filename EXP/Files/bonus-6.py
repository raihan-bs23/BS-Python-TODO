contents = ["This code first reads the data from the CSV file and stores it in a list." ,
            "It then prints the todo list with an index for each item." ,
            "The user is prompted to enter the index of the item to edit and the new todo."]
filenames = ["test.txt", "test1.txt", "test2.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../TEST/{filename}", 'w')
    file.write(content)