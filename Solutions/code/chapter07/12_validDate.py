def main():

    date = input("Input date to check (XX/XX/XXXX). ").split("/")

    month = int(date[0])
    day = int(date[1])
    year = int(date[2])

    daysInMonth = [31,28,31,30,31,30,31,31,30,31,30,31]

    if day == daysInMonth[month+1]:
        print("Date is valid.")
    else:
        print("Date is not valid.")

main()