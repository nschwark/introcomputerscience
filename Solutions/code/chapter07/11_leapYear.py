def main():
    year = int(input("What year would you like to check is a leap year? "))

    if (year % 100) == 0 and (year % 400) == 0:
        print("It is a leap year.")
    elif (year % 4 ) == 0:
        print("It is a leap year.")
    else:
        print("It is not a leap year.")
        
main()