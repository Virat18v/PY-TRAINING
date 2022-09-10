num1 = int(input("enter num 1 "))
num2 = int(input("enter num 2 "))
num3 = int(input("enter num 3 "))
num4 = int(input("enter num 4 "))

if (num1 > num4):
    f1 = num1
else:
    f1 = num4
if (num2 > num2):
    f2 = num2
else:
    f2 = num1
if(f1 > f2):
    print(str(f1)+"is greatest")
else:
    print(str(f2)+"is greatest")
