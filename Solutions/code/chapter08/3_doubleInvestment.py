def main():
    apr = eval(input("Enter the annual interest rate: "))

    principal = 500
    years = 0
    doubleInvestment = principal * 2

    while principal <= doubleInvestment:
        principal = principal * (1 + apr)
        years = years + 1

    print("It took {0} years to double investment".format(years))
    print(principal)

main()