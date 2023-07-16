"""
    returns true if the given function doesn't have the letter e
"""
def has_no_e(word):
    for letter in word.lower():
        if letter == "e":
            return False
    return True
def main():
    fin = open("words.txt", "r")
    for word in fin:
        word = fin.readline().strip()
        if has_no_e(word):
            print(word)
main()