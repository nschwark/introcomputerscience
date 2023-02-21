def acronym(phrase):
    words = phrase.split(" ")

    acro = ""

    for ch in words:
        acro = acro + ch[0].upper()

    return acro

def main():
    phrase = input("Enter phrase: ")
    print("{0}".format(acronym(phrase)))

main()