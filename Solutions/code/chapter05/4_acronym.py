def main():
    phrase = input("Enter phrase: ")
    words = phrase.split(" ")

    for ch in words:
        print("{0}".format(ch[0].upper()), end="")

main()