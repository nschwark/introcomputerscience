# rballAltShutout.py
#    Simulation of a racquetball game

from random import random

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB, shutoutA, shutoutB = simNGames(n, probA, probB)
    printSummary(winsA, winsB, shutoutA, shutoutB)

def printIntro():
    print("This program simulates a game of racquetball between two")
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

def simNGames(n, probA, probB):
    # Simulates n games of racquetball between players whose
    #    abilities are represented by the probability of winning a serve.
    # Returns number of wins for A and B
    winsA = winsB = 0
    shutoutA = shutoutB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB, i)
        if scoreA ==15 and scoreB == 0:
            shutoutA = shutoutA + 1
        elif scoreB == 15 and scoreA == 0:
            shutoutb = shutoutB + 1

        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB, shutoutA, shutoutB

def simOneGame(probA, probB, i):
    # Simulates a single game or racquetball between players whose
    #    abilities are represented by the probability of winning a serve.
    # Returns final scores for A and B
    
    if (i%2) == 0:
        serving = "B"
    else:
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

def gameOver(a, b):
    # a and b represent scores for a racquetball game
    # Returns True if the game is over, False otherwise.
    return a==15 or b==15

def printSummary(winsA, winsB, shutoutA, shutoutB):
    # Prints a summary of wins for each player.
    n = winsA + winsB
    print("\nGames simulated:", n)
    print("Wins for A: {0} ({1:0.1%})".format(winsA, winsA/n))
    print("Wins for B: {0} ({1:0.1%})".format(winsB, winsB/n))
    print("Shutouts for A: {0} ({1:0.1%})".format(shutoutA, shutoutA/n))
    print("Shutouts for B: {0} ({1:0.1%})".format(shutoutB, shutoutB/n))

if __name__ == '__main__': main()
