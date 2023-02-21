import math

height, degrees = eval(input("Enter the height need to reach and angle desired: "))

radians = (math.pi/180)*degrees
length = height/math.sin(radians)

print("The length of ladder needed: ", length)