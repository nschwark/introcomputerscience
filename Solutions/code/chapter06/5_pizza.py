import math

def areaPizza(r):
    A = math.pi*(r**2)
    return A

def costSquareInch(p, r):
    cpsi = p/areaPizza(r)
    return cpsi

def main():
    r = (float(input("Please enter the diameter of pizza: ")))/2
    p = float(input("Please enter the price of pizza: "))

    print("The cost per square inch of the pizza is: ", costSquareInch(p,r))

main()