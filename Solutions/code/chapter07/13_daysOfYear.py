def validDate(day,month):
    daysInMonth = [31,28,31,30,31,30,31,31,30,31,30,31]

    if day <= daysInMonth[month+1]:
        return "Valid"
    else:
        return "Not valid"

def leapYear(year):
    
    if (year % 100) == 0 and (year % 400) == 0:
        return "Valid"
    elif (year % 4 ) == 0:
        return "Valid"
    else:
        return "Not valid"


def main():

    date = input("Input date to check (XX/XX/XXXX). ").split("/")

    month = int(date[0])
    day = int(date[1])
    year = int(date[2])

    dayNum = (31 * (month - 1)) + day

    if str(validDate(day,month)) == "Valid":

        if leapYear(year) == "Valid" and month > 2:

            print("The day number is ", ((dayNum - ((4 * month) + 23) // 10) + 1))

        elif month > 2:

            print("The day number is ", (dayNum - ((4 * month) + 23) // 10))

        else:
            print("The day number is ", dayNum)
    else:
        print("Your date is not valid.")

main()