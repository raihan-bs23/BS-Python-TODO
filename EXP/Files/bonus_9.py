password = input("Enter password to check - ")

passLen = len(password)
result = []
if passLen >= 8:
    result.append(True)
else:
    result.append(False)

digit = False
for i in password:
    if i.isdigit():
        digit = True
result.append(digit)

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True
result.append(uppercase)

if all(result):
    print("Strong Password !")
else:
    print("Weak Password !")
