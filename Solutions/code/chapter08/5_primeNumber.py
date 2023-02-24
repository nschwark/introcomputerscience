import math

def main():

    number = int(input("Enter a number: "))

    squareRootNumber = int(math.sqrt(number))

    while squareRootNumber <= number and squareRootNumber >= 2:

        if (number % squareRootNumber) != 0 and squareRootNumber != 2:
            squareRootNumber = squareRootNumber - 1
        elif squareRootNumber == 2 and (number % squareRootNumber) != 0:
            print("Number is prime.")
            squareRootNumber = 0
        elif (number % squareRootNumber) == 0:
            print("Number is not a prime.")
            squareRootNumber = 0

main()
        