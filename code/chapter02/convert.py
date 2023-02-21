# convert.py
#     A program to convert Celsius temps to Fahrenheit
# by: Susan Computewell

def main():
    celsius = 0

    for i in range(11):
        # celsius = eval(input("What is the Celsius temperature? "))
        
        fahrenheit = 9/5 * celsius + 32
        print("The temperature in celsius", celsius, "is", fahrenheit, "degrees Fahrenheit.")
        celsius = celsius + 10

main()
