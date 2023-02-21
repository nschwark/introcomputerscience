def main():
    word = input("Enter word to encrypt: ")
    key = int(input("Enter encryption key: "))
    total = ""

    for ch in word:
        #print(ord(ch.lower())-96, end=" ")
        #print(ch)
        cryCh = chr(ord(ch) + key)
        total = total + cryCh
        #print(numb)
    print(total)
main()