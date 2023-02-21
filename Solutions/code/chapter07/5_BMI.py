def main():
    
    weight = float(input("Enter your weight in pounds: "))
    height = float(input("Enter your height in inches: "))

    bmi = (weight * 720) / (height ** 2)

    if bmi > 25:
        print("Your BMI is above the healthy range.")
    elif bmi <= 25 and bmi >= 19:
        print("Your BMI is within the healthy range.")
    elif bmi < 19:
        print("Your BMI is below the healthy range.")

main()