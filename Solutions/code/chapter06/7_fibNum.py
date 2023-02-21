def fibonacci(n):
    sum1,sum2 = 1,1

    for i in range(n-1):
        sum3 = sum1 + sum2
        sum1 = sum2
        sum2 = sum3

    return sum1

def main():
    nth = int(input("Please enter the nth number and it will calculate Fibonacci number: "))
    print("The Fibonacci number is: ", fibonacci(nth))

main()