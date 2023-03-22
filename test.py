
f = []
g = []
for i in range(1, 100):
    if i % 2 == 0:
        f.append(i)
    else:
        g.append(i)

print("Odd List = ", g)
print("Even List = ", f)

lst = []
vowel = ['a', 'e', 'i', 'o', 'u']
for i in range(2):
    lst.append(input("Enter Name of your friends - "))

for i in lst:
    count = 0
    for j in vowel:
        if j in i:
            print(j)
            count = count + 1

    print(f"Your Friend-{i} has {count} vowel")



for i in range(10):
    print("Assalamualaikum")