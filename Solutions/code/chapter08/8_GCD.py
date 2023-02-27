def main():

    n = int(input("Enter n: "))
    m = int(input("Enter m: "))

    while m != 0:

        n, m = m, n%m

    print(n)

main()