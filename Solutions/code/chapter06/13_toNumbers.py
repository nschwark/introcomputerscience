def toNumbers(strList):
    x = 0

    for strNum in strList:
        strList[x] = float(strNum)
        x = x + 1

    return strList

def main():

    strList = ["1", "2", "3"] 
    print(toNumbers(strList))

main()