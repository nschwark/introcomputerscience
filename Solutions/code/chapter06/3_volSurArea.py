import math

def sphereVolume(radius):
    V = (4/3)*math.pi*(radius**3)
    return V

def sphereArea(radius):
    A = 4*math.pi*(radius**2)
    return A

def main():
    radius = float(input("Please enter the radius: "))

    print("Volume is: ", sphereVolume(radius), "and surface area is: ", sphereArea(radius))

main()