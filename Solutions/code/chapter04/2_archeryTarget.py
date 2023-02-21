from graphics import *

def main():
    win = GraphWin()

    shape = Circle(Point(100,100), 10*5)
    shape.setOutline('white')
    shape.setFill("white")
    shape.draw(win)
    shape = Circle(Point(100,100), 10*4)
    shape.setOutline('black')
    shape.setFill("black")
    shape.draw(win)
    shape = Circle(Point(100,100), 10*3)
    shape.setOutline('blue')
    shape.setFill("blue")
    shape.draw(win)
    shape = Circle(Point(100,100), 10*2)
    shape.setOutline('red')
    shape.setFill("red")
    shape.draw(win)
    shape = Circle(Point(100,100), 10)
    shape.setOutline('yellow')
    shape.setFill("yellow")
    shape.draw(win)
    win.getMouse()

main()