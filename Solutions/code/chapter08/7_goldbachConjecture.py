import math

def primeNumbers(number):
    primes = [3,2]
    
    while number > 2:

        squareRootNumber = int(math.sqrt(number))

        while squareRootNumber <= number and squareRootNumber >= 2:

            if (number % squareRootNumber) != 0 and squareRootNumber != 2:
                squareRootNumber = squareRootNumber - 1
            elif squareRootNumber == 2 and (number % squareRootNumber) != 0:
                #print(number)
                primes.append(number)
                #print("Number is prime.")
                squareRootNumber = 0
            elif (number % squareRootNumber) == 0:
                #print("Number is not a prime.")
                squareRootNumber = 0
        number = number - 1
    
    return primes

def main():
    
    number = int(input("Enter an even number: "))
    total, total2 = number, number
    listNum, listNum2 = 0,0

    if (number % 2) == 0:

        primeList = primeNumbers(number)
        primeList.sort(reverse=True)
        print(primeList)

    while total != 0:
       
        #print(listNum)

        if listNum != len(primeList):
            total = number - primeList[listNum]
            #print(total)
        else:
            listNum = 0

        while total2 != 0:
            
            if listNum2 != len(primeList):
                total2 = total - primeList[listNum2]
                #print(total2)
            else:
                total2 = 0
                listNum2 = 0

            if total2 == 0:
                total = 0

            listNum2 = listNum2 + 1
        
        
        print("ListNum2: " , listNum2)
        listNum = listNum + 1

    print(len(primeList))
    print(listNum, listNum2)
    print(primeList[listNum], primeList[listNum2])


main()