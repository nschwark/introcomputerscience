def main():

    score = int(input("Enter the number of credit earned: "))

    if score >= 26:
        print("Your standing is {0}".format("Senior"))
    elif score < 26 and score >= 16:
        print("Your standing is {0}".format("Junior"))
    elif score < 16 and score >= 7:
        print("Your standing is {0}".format("Sophmore"))
    elif score < 7:
        print("Your standing is {0}".format("Freshman"))

main()