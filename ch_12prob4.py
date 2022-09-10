# A program to checking a/b where a & b are integers
a = int(input("Enter number a: "))
b = int(input("Enter number b: "))

try:
    print(a/b)
except:
    print("Infinite")