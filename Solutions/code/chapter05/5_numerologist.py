def main():
    name = input("Enter name: ")
    total = 0

    for ch in name:
        
        numb = ord(ch.lower())-96
        total = total + numb
        
    print(total)
main()