def main():
    hours = float(input("Enter the amount of hours worked: "))
    wage = float(input("Enter the wage: "))

    overTime, overTimeHours = 0, 0
    
    if hours > 40:
        overTimeHours = hours - 40
        overTime = ((overTimeHours) * (wage * 1.5))

    total = (hours - overTimeHours) * wage

    print("The total wages for the week are: ${0:0.2f}".format(total + overTime))

main()