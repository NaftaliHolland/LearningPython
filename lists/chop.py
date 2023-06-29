#A function that takes a list and modifies it by removing the first and last elements

def chop(t):
    del t[0]
    del t[-1]
    return None
def main():
    t = [1, 2, 3, 4]
    chop(t)
    print(t)
main()