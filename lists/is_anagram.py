#A function that takes two strings and returns true if the two words are anagrams

def is_anagram(s1, s2):
    s1 = list(s1.lower())
    s2 = list(s2.lower())

    s1.sort()
    s2.sort()

    if s1 == s2:
        return True
    return False
def main():
    s = "soil"
    ss = "loIs"
    print(is_anagram(s, ss))

main()