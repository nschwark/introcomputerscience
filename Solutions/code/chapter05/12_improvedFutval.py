def main():
    print("This program calculates the future value")
    print("of a 10-year investment.")

    principal = eval(input("Enter the amount each year: "))
    apr = eval(input("Enter the annual interest rate: "))
    year = eval(input("Enter the number of years: "))
    investment = principal

    print("{0:5}   {1:^8}".format("Year","Value"))
    print("----------------")

    for i in range(year):
        principal = principal * (1 + apr)
        principal = principal + investment
        print("{0:^5}   ${1:^6.2f}".format(i,principal))

    print("The value in", year, "years is:", principal)

main()