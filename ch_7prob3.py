num=int(input("enter num"))
prime=True
for i in range(2,num):
 if(num%i==0):
        prime=False
        break
if prime:
 print("this num is prime")
else:
    print("this num is not prime")
