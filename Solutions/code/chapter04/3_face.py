from graphics import *

def main():
    win = GraphWin(width=500, height=500)
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    shape = Circle(Point(4,5), 1)
    shape.setOutline('black')
    shape.setFill("black")
    shape.draw(win)
    shape = Circle(Point(6,5), 1)
    shape.setOutline('black')
    shape.setFill("black")
    shape.draw(win)
    win.getMouse()
main()