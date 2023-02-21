def calAfterHours(hours,minutes):
    afterHoursCharges = (hours * 1.75) + ((minutes / 60) * 1.75)
    return afterHoursCharges

def calRegCharges(totalHours, totalMinutes):
    charges = (float(totalHours) * 2.5) + ((float(totalMinutes)/60)* 2.5)
    return charges

def main():
    startTime = input("What time did you start? ").split(":")
    endTime = input("What time did you end? ").split(":")

    startAmPm = startTime[1].split(" ")
    endAmPm = endTime[1].split(" ")
    startHour = float(startTime[0])
    startMin = float(startAmPm[0])
    endHour = float(endTime[0])
    endMin = float(endAmPm[0])

    totalMinutes = endMin + startMin
    
    if startAmPm == endAmPm or endHour == 12:
        totalHours = endHour - startHour
    else:
        totalHours = (endHour) + (12 - startHour)

    if endHour > 8 and endHour != 12:
        afterHours = endHour - 9
        print("${0:0.2F}".format(calAfterHours(afterHours,endMin)+calRegCharges(totalHours-afterHours, 0)))
    else:
        print("${0:0.2F}".format(calRegCharges(totalHours, totalMinutes)))


main()