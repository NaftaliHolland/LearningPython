#This program implements the ceaser cypher algorithm

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                  'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encode(shift, word):
    encrypted_word = ""
    word = list(word)
    for i in word:
        index = alphabets.index(i) + shift
        if index > len(alphabets) - 1:
            index = index - len(alphabets)
        encrypted_word += alphabets[index]
    return encrypted_word

def decode(shift, word):
    decrypted_word = ""
    for i in word:
        index = alphabets.index(i) - shift
        decrypted_word += alphabets[index]
    return decrypted_word

def ceaser_cypher():
     while True:
        encode_decode = input("Do you want to encode or decode :").lower()
        if encode_decode == "encode":
            word = input("Type the word you want to encode : ").lower()
            shift = int(input("Type the shift number "))
            return encode(shift, word)

        elif encode_decode == "decode":
            word = input("Type the word you want to decrypt : ").lower()
            shift = int(input("Type the shift number "))
            return decode(shift, word)
        else:
            print("Enter a valid input encode or decode ")
def main():
    while True:
        print(ceaser_cypher())
        play_on = input("Enter yes to continue and q to quit ")
        if play_on == "q":
            print("Continue being safe :)")
            quit()
main()