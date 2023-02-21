def main():
    fullName = input("Enter full name: ")
    names = fullName.split(" ")
    total = 0
    charTotal = 0

    for name in names:
        for ch in name:
            charTotal = charTotal + 1
        total = total + 1            
    print(charTotal/total)
main()