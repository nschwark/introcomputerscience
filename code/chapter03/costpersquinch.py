import math

d = float(input("Please enter the diameter of pizza: "))
p = float(input("Please enter the cost of pizza: "))
r = d/2
A = math.pi*(r**2)
cps = p/A

print("The cost per square inch: ", cps)