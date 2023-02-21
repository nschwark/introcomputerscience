def main():
    fullName = input("Enter full name: ")
    names = fullName.split(" ")
    total = 0

    for name in names:
        total = total + 1            
    print(total)
main()