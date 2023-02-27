def main():
    
    odoList = []    
    gasList = [0]
    MPGList = []

    num = 0
    
    startOdometer = input("Enter initial odometer reading: ")

    odoList.append(startOdometer)
    
    while True:

        legInformation = input("Enter odometer and amount of gas used: ").split(" ")
        
        if legInformation != ['']:
            odometer = int(legInformation[0])
            gasUsed = int(legInformation[1])
        else:
            break

        odoList.append(odometer)
        gasList.append(gasUsed)

    while True:

        if num == int(len(odoList)-1):
            break
        else:

            miles = int(odoList[num + 1]) - int(odoList[num])
            gallons = int(gasList[num + 1])

            mpg = miles/gallons
            MPGList.append(mpg)

            num = num + 1
    
    print(MPGList)
    
    totalMPG = 0

    num = 0

    for i in MPGList:

        totalMPG = totalMPG + float(MPGList[num])

        num = num + 1

    totalAvgMPG = totalMPG / int(len(MPGList))
    print(totalAvgMPG)

main()