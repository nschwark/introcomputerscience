def main():
    
    speedLimit = float(input("Enter the speed limit: "))
    clockedSpeed = float(input("Enter your clocked speed: "))

    if clockedSpeed <= speedLimit:
        print("Speed was legal.")
    elif clockedSpeed > speedLimit:
        
        overSpeed = clockedSpeed - speedLimit
        fine = 50 + (overSpeed * 5)
        
        if clockedSpeed >= 90:
            fine = fine + 200

        print("You speed was over the limit and your fine is ${0:0.2F}".format(fine))
main()