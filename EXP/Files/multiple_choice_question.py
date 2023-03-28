'''
complex data structure in python with list and dictionary at a time
extract question from json file
'''
import json
import csv
import datetime

filename = 'multiple_choice_question_data.csv'
fields = ["timestamp", "username", "ID", "correct answer", "wrong answer", "marks"]

'''
load question data from json file
'''
with open("question.json", 'r') as file:
    content = file.read()
data = json.loads(content)

'''
load user data from a json file
'''
with open("user_info.json", 'r') as user:
    info = user.read()
user_data = json.loads(info)

user_name = input("Enter Your User Name : ")
user_id = input("Enter Your User ID : ")

for user_info in user_data:
    if user_info['username'] == user_name.strip() and user_info["id"] == user_id.strip():
        print("*********** BS QUIZ **********")
        l = 'A'
        marks = 0
        correct_ans = 0
        wrong_ans = 0
        for j, question in enumerate(data):
            print(f"({chr(ord(l) + j)}) {question['question text']}")
            for i, alternative in enumerate(question["alternatives"]):
                print(f"{i + 1}- {alternative}")
            user_choice = int(input("Enter Your Choice : "))
            question['user_choice'] = user_choice

            if question['user_choice'] == question['correct Answer']:
                # print(question['correct Answer'])
                correct_ans = correct_ans + 1
                print("Correct Answer !!")
                marks = marks + 10
            else:
                wrong_ans = wrong_ans + 1
                print("Wrong Answer !!")

        print("Total Marks = ", marks, "out of", len(data) * 10)
        for question in data:
            message = f"Your Answer: {question['user_choice']},  " \
                      f"Correct Answer: {question['correct Answer']}"
            print(message)

        try:
            with open(filename, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                rows = list(reader)
        except FileNotFoundError:
            rows = []

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        rows.append({"timestamp": timestamp, "username": user_name, "ID": user_id, "correct answer": correct_ans,
                     "wrong answer": wrong_ans, "marks": marks})
        with open(filename, 'w', newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)
            print("1 row affected !")


