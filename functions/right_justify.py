def right_justify(s):
    for i in range(70 - len(s)):
        print(" ", end = "")
    print(s)

def main():
    s = "Hello"
    right_justify(s)

main()