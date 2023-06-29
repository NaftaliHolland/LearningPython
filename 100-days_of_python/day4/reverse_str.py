
string = input("Write something :")
reversed_str = ""
length = len(string)
for em, char in enumerate(string):
    reversed_str += string[length -1]
    length -= 1
print(reversed_str)