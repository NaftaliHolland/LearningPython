"""
    reads a file words.txt and prints words with more than 5 characters
"""

fin = open("words.txt", "r")

for word in fin:
    word = fin.readline().strip()
    if len(word) > 5:
        print(word)
