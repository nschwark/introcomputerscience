nth = int(input("Please enter the nth number and it will sum them: "))
sum = 0

for i in range(1,nth+1):
    sum = sum + (i**3)
    print(sum)

print(sum)