import math

seconds = int(input("Enter the number of seconds from lighning strike to the sound of thunder: "))

distance = (1100/5280) * seconds

print("The distance to lighning strike is: ", distance, " miles")