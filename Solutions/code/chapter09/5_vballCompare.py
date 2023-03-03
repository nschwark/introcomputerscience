# vball.py
#    Simulation of a racquetball game

from random import random

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB,"Standard")
    rallyWinsA, rallyWinsB = simNGames(n, probA, probB, "Rally")
    printSummary(winsA, winsB)
    printSummary(rallyWinsA, rallyWinsB)
    compareTypes(probA, probB, winsA, winsB, rallyWinsA, rallyWinsB)

def printIntro():
    print("This program simulates a game of volleyball between two")
    print('players called "A" and "B".  The abilities of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving. Player A always")
    print("has the first serve.")

def getInputs():
    # Returns the three simulation parameters
    a = float(input("What is the prob. player A wins a serve? "))
    b = float(input("What is the prob. player B wins a serve? "))
    n = int(input("How many games to simulate? "))
    return a, b, n

def simNGames(n, probA, probB, type):
    # Simulates n games of racquetball between players whose
    #    abilities are represented by the probability of winning a serve.
    # Returns number of wins for A and B
    winsA = winsB = 0
    for i in range(n):
        if type == "Standard":
            scoreA, scoreB = simOneGame(probA, probB)
        elif type == "Rally":
            scoreA, scoreB = simOneGameRally(probA, probB)

        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
        print("Game {0} the score for A is {1} and the score for B is {2}".format(i,scoreA,scoreB))
    return winsA, winsB

def simOneGame(probA, probB):
    # Simulates a single game or racquetball between players whose
    #    abilities are represented by the probability of winning a serve.
    # Returns final scores for A and B
    serving = "A"
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
    return scoreA, scoreB

def simOneGameRally(probA, probB):
    # Simulates a single game or racquetball between players whose
    #    abilities are represented by the probability of winning a serve.
    # Returns final scores for A and B
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):
        if random()*probA > random()*probB:
            scoreA = scoreA + 1
        else:
            scoreB = scoreB + 1   
    return scoreA, scoreB

def gameOver(a, b):
    # a and b represent scores for a racquetball game
    # Returns True if the game is over, False otherwise.
    if a==15 and (a-b) >= 2:
        return True
    elif b==15 and (b-a) >=2:
        return True
    #return a==15 or b==15

def compareTypes(probA, probB, winsA, winsB, winsRallyA, winsRallyB):
    if probA > probB:
        betterTeam = probA
        betterStandardWins = winsA
        betterRallyWins = winsRallyA
    else:
        betterTeam = probB
        betterStandardWins = winsB
        betterRallyWins = winsRallyB


    if betterTeam and betterRallyWins > betterStandardWins:
        print("Rally magnifies")
    elif betterTeam and betterRallyWins == betterStandardWins:
        print("Rally no effect")
    else:
        print("Rally reduces")


def printSummary(winsA, winsB):
    # Prints a summary of wins for each player.
    n = winsA + winsB
    print("\nGames simulated:", n)
    print("Wins for A: {0} ({1:0.1%})".format(winsA, winsA/n))
    print("Wins for B: {0} ({1:0.1%})".format(winsB, winsB/n))

if __name__ == '__main__': main()
