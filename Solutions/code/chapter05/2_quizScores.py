def main():
    # get the day month and year as numbers
    score = int(input("Enter the score number: "))

    scores = ["F", "F", "D", "C", 
              "B", "A"]

    scoresStr = scores[score]

    print("Your grade is {0}".format(scoresStr))         

main() 