def grade(score):
    
    scoreDivide = int(score / 10)
    scores = ["F", "F","F", "F","F", "F","D", "C", 
              "B", "A", "A"]

    scoresStr = scores[scoreDivide]
    return scoresStr

def main():
    score = int(input("Enter the score number: "))
    print("Your grade is {0}".format(grade(score)))

main()