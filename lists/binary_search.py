#Binary search implementation

def binary_search(value, list):
    if len(list) == 0:
        print("{} not in list".format(value))
        return
    mid = int(len(list) / 2)
    if value == list[mid]:
        print("{} Found".format(value))
        return
    elif value < list[mid]:
        binary_search(value, list[:mid])
    elif value > list[mid]:
        binary_search(value, list[mid:])

def main():
    t = [1, 3, 4, 5, 77, 6, 4, 8, 9, 4]
    t.sort()
    binary_search(2, t)
main()