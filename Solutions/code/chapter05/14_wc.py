def main():

    fname = input("Enter filename: ")
    infile = open(fname,"r")

    chrTotal, wordsTotal, lineTotal = 0,0,0

    for line in infile:
        lineTotal = lineTotal + 1
        words = line.split(" ")
        for word in words:
            wordsTotal = wordsTotal + 1
            chrs = word.replace("\n","")
            for chr in chrs:
                chrTotal = chrTotal + 1
    
    print(chrTotal, wordsTotal, lineTotal)
main()