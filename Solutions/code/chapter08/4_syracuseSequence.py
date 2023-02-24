def main():

    number = int(input("Input number to start sequence: "))
    output = ""

    while number != 1:

        if (number % 2) != 0:
             number = int((3*number) + 1)
        else:
            number = int(number / 2)

        output = output + "{0}, ".format(str(number))

    
    replacementStr = "."
    output = output[:-2] + replacementStr
    print(output)

main()