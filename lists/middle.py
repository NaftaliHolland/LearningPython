#A function takes a list and returns a new list that contains all but the first and last elements

def middle(t):
    t = t[1 : -1]

    return t

def main():
    t = [1, 2, 3, 4, 5, 6, 8]
    print(middle(t))

main()