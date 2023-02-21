nth = int(input("How many numbers do you want to sum? "))
total = 0

for i in range(nth):
    num = float(input("Enter number: "))

    total = total + num

print(total/nth)