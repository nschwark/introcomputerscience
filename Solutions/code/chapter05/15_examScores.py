from graphics import *

def main():

    fname = "examScores.txt"
    infile = open(fname,"r")

    numLines = 0
    lineNum = 0

    for line in infile:
        numLines = numLines + 1

    infile.close()

    win = GraphWin("Investment Growth Chart", 320, 320)
    win.setCoords(-50.0, -1.0, 100.0, numLines*10)
    win.setBackground("white")
    textY = 2.5
    barY = 0

    infile = open(fname,"r")

    for line in infile:

        words = line.split(" ")

        message = Text(Point(-25, textY), words[0])
        message.draw(win)
        
        bar = Rectangle(Point(0, barY), Point(words[1], barY + 5))
        bar.setFill("green")
        #bar.setWidth(2)
        bar.draw(win)

        barY = barY + 10
        textY = textY + 10

        print(words[:])

    win.getMouse()

main()