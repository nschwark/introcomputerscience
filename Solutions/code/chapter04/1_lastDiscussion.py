from graphics import *

def main():
    win = GraphWin()
    shape = Rectangle(Point(50,50), Point(75,75))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        newShape = shape.clone()
        newShape.move(dx,dy)
        newShape.draw(win)
    message = Text(Point(5, 0.5), "Click anywhere to quit.")
    message.draw(win)
    win.getMouse()
main()