def main():

    score = int(input("Enter the score number: "))

    if score == 5:
        print("Your grade is {0}".format("A"))
    elif score == 4:
        print("Your grade is {0}".format("B"))
    elif score == 3:
        print("Your grade is {0}".format("C"))
    elif score == 2:
        print("Your grade is {0}".format("D"))
    elif score <= 1:
        print("Your grade is {0}".format("F"))

main()

    