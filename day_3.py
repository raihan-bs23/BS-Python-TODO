
todo = []
while True:
    userAction = input("Type add, show, exit -")
    userAction = userAction.strip().lower()
    # strip for removing all the whitespace and lower for convert all the char to lowercase
    match userAction:
        case 'add':
            uInput = input("Enter a Todo - ")
            todo.append(uInput)
        case 'show':
            print("************* TO DO List ***********\n")
            for counter, i in enumerate(todo):
                i = i.title() # make all the word in title format
                print(f"{counter+1}. {i} ")
        case 'exit':
            break
        case whatever:
            print("You have enter unknown command !!")
print("Program exit. Bye !")