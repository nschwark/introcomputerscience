import math

a, b, c = eval(input("Enter the length of each side of the triangle: "))

s = (a+b+c)/2
Area = math.sqrt(s*((s-a)*(s-b)*(s-c)))

print("The area of the traingle is: ", Area)