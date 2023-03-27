day = input("Enter the current date - ")
mood = input("state you mood status in range (1-10) - ")
thoughts = input("Enter your thoughts for the day - ")
with open(f"Thought Note/{day}.txt", "w") as file:
    file.write(mood + 2*"\n")
    file.write(thoughts)