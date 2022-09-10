# n!=1 x 2 x 3 x .....x n
# 5!=1 x 2 x 3 x 4 x 5
num = int(input("enter the number"))
factorial = 1
for i in range(1, num+1):
    factorial = factorial*i
print(f"the factorial of {num} is {factorial}")
