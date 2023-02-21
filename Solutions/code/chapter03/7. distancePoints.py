import math

x1, y1 = eval(input("Enter the x,y coordinates of first point: "))
x2, y2 = eval(input("Enter the x,y coordinates of second point: "))

distance  = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("The distance between two points is: ", distance)