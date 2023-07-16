def createPhoneNumber(numbers):

    phoneNumber = "("
    for i in numbers[:3]:
        phoneNumber += str(i)
    phoneNumber += ") "

    for i in numbers[3:6]:
        phoneNumber += str(i)
    phoneNumber += "-"

    for i in numbers[6:]:
        phoneNumber += str(i)

    return phoneNumber

def main():
    print(createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

main()