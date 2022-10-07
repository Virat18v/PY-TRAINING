def decimal_to_binary():
    n = int(input("Enter number :* "))
    while n > 0:
        r = n % 2
        print(r)
        n=n//2


decimal_to_binary()
