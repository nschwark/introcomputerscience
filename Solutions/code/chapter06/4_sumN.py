def sumN(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    return sum

def sumNCubes(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + (i**3)
    
    return(sum)

def main():
    
    n = int(input("Please enter the nth number and it will sum them: "))
    print(sumN(n))
    print(sumNCubes(n))

main()