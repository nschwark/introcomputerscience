def main():
    print("This program illustrates a chaotic function")
    #x = eval(input("Enter a number between 0 and 1: "))
    #y = eval(input("Enter a number between 0 and 1: "))
    n = eval(input("How many numbers should I print? "))

    fname = input("Enter filename: ")
    infile = open(fname,"r")
    #data = infile.read()

    outfileName = input("What file should the usernames go in? ")
    outfile = open(outfileName, "w")

    for line in infile:
        inFileX,inFileY = line.split(",")

        x = float(inFileX)
        y = float(inFileY)

        print("{0}  {1:^8.6}     {2:^8.6}".format("Index",x,y), file=outfile)
        print("----------------------------", file=outfile)
    
        for i in range(n):
            x = 3.9 * x * (1 - x)
            y = 3.9 * y * (1 - y)
            print("{0:^5}  {1:^8.6f}     {2:^8.6f}".format(i+1,x,y), file=outfile)

main()