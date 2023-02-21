# futval.py
#    A program to compute the value of an investment
#    carried 10 years into the future

def main():
    print("This program calculates the future value")
    print("of a 10-year investment.")

    principal = eval(input("Enter the amount each year: "))
    apr = eval(input("Enter the annual interest rate: "))
    year = eval(input("Enter the number of years: "))
    investment = principal

    for i in range(year):
        principal = principal * (1 + apr)
        principal = principal + investment

    print("The value in", year, "years is:", principal)

main()
