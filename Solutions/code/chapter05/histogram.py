from graphics import *

def main():

    fname = "histogram.txt"
    infile = open(fname,"r")
    data = infile.read()

    win = GraphWin("Investment Growth Chart", 500, 320)
    win.setCoords(0, -2.0, 110.0, 20.0)
    win.setBackground("white")

    for i in range(0,11):
        count = data.count(str(i))
        print(count)

        message = Text(Point(i*10+5, -1), i)
        message.draw(win)
        
        bar = Rectangle(Point(i*10+2.5, 0), Point(i*10+7.5, count))
        bar.setFill("green")
        #bar.setWidth(2)
        bar.draw(win)
    win.getMouse()

main()