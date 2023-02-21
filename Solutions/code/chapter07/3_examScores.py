def main():

    score = int(input("Enter the score percentage: "))

    if score <= 100 and score >= 90:
        print("Your grade is {0}".format("A"))
    elif score <= 89 and score >= 80:
        print("Your grade is {0}".format("B"))
    elif score <= 79 and score >= 70:
        print("Your grade is {0}".format("C"))
    elif score <= 69 and score >= 60:
        print("Your grade is {0}".format("D"))
    elif score < 60:
        print("Your grade is {0}".format("F"))

main()