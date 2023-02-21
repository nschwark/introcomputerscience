def main():

    age = int(input("What is your age? "))
    citizenship = int(input("How long have you been a US citizen? "))

    if age >= 30:

        if citizenship >= 9:
            print("Are are eligible for the Senate and House")
        elif citizenship >= 7:
            print("Are are eligible for the House")
        else:
            print("You are not eligible for the Senate or House")
    elif age >= 25:
        if citizenship >= 7:
            print("Are are eligible for the House")
        else:
            print("You are not eligible for the Senate or House")
    else:
        print("You are not eligible for the Senate or House")

main()