#A function that takes a list and returns true if the list is sorted in asscending order and false if not

def is_sorted(t):
    new = t[:]
    t.sort()
    if new == t:
        return True
    return False

def main():
    print(is_sorted(['b', 'a']))
main()