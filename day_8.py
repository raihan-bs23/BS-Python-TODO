'''
this program is to read a text file from a directory and read the content
of the text file. then seperate all the word from the text.
then find all the vowel from each word and replace all the vowel with *
'''
vowel = ['a', 'e', 'i', 'o', 'u']
with open("EXP/TEST/test.txt") as file:
    temp = file.read()
    words = temp.split()
    for i in words:
        for j in i:
            if j in vowel:
                i = i.replace(j, "*")
        print(i)

print(temp.title())