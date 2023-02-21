import math

r = (float(input("Please enter the diameter of pizza: ")))/2
p = float(input("Please enter the price of pizza: "))

A = math.pi*(r**2)

print("The cost per square inch of the pizza is: ", p/A)