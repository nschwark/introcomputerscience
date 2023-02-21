nth = int(input("Please enter the nth number and it will calculate Fibonacci : "))
sum1,sum2 = 1,1

for i in range(nth-1):
    sum3 = sum1 + sum2
    sum1 = sum2
    sum2 = sum3

print(sum1)