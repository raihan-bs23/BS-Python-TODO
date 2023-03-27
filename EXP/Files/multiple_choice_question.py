'''
complex data structure in python with list and dictionary at a time
'''
import json

with open("../Files/Thought Note/question.json", 'r') as file:
    content = file.read()

data = json.loads(content)
l = 'A'
marks = 0
for j, question in enumerate(data):
    print(f"({chr(ord(l)+j)}) {question['question text']}")
    for i, alternative in enumerate(question["alternatives"]):
        print(f"{i+1}- {alternative}")
    user_choice = int(input("Enter Your Choice : "))
    question['user_choice']=user_choice
    if question['user_choice'] == question['correct Answer']:
        print(question['correct Answer'])
        marks = marks + 10

print("Total Marks = ", marks, "out of", len(data)*10)
for question in data:
    message = f"Your Answer: {question['user_choice']},  "\
                f"Correct Answer: {question['correct Answer']}"

    print(message)

    print("hello")


