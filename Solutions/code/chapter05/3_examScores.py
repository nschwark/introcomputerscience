def main():
    score = int(input("Enter the score number: "))
    scoreDivide = int(score / 10)
    scores = ["F", "F","F", "F","F", "F","D", "C", 
              "B", "A", "A"]

    scoresStr = scores[scoreDivide]

    print("Your grade is {0}".format(scoresStr))         

main() 