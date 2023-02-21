import math

nth = int(input("Please enter the nth number and it will calculate Pi: "))
total,piesum = 0,0
neg = -1

for i in range(1,(2*nth+1),2):
    neg = neg * -1
    num = i * neg
    piesum = piesum + (4/num)

print(piesum)
print(math.pi)