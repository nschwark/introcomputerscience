def main():
    fullName = input("Enter full name: ")
    names = fullName.split(" ")
    total = 0

    for name in names:
        for ch in name:
            #print(ord(ch.lower())-96, end=" ")
            #print(ch)
            numb = ord(ch.lower())-96
            total = total + numb
            #print(numb)
    print(total)
main()