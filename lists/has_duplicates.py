#A function that takes a list and returns true if there are any duplicates in the list

def has_duplicates(t):
    new = t[:]
    new.sort()

    for em, i in enumerate(new):
        if em == len(new) - 1:
            return False
        if new[em] == new[em + 1]:
            return True
    return False

def main():
    print(has_duplicates([1,4,3,7,8,4]))

main()
    