import math

x1, y1 = eval(input("Enter the x,y coordinates of first point: "))
x2, y2 = eval(input("Enter the x,y coordinates of second point: "))

slope = (y2 - y1)/(x2 - x1)

print("The slope is: ", slope)