def main():

    year = int(input("What year do you want to calculate the date of Easter? "))

    a = year % 19
    b = year % 4
    c = year % 7
    d = ((19 * a) + 24) % 30
    e = ((2 * b) + (4 * c) + (6 * d) + 5) % 7

    if year == 1954 or year == 1981 or year == 2049 or year == 2076:
        easter = 22 + d + e
        if easter > 31:
            print("The date of Easter is April {0}".format(easter - 31- 7))
        else: 
            print("The date of Easter is March {0}".format(easter - 7))
    elif year >= 1900 and year <= 2099:
        easter = 22 + d + e
        if easter > 31:
            print("The date of Easter is April {0}".format(easter - 31))
        else: 
            print("The date of Easter is March {0}".format(easter))
    else:
        print("Date not between 1900 and 2099.")

main()