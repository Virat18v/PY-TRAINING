sub1 = int(input("enter sub1 marks "))
sub2 = int(input("enter sub2 marks "))
sub3 = int(input("enter sub3 marks "))

if(sub1 < 33 or sub2 < 33 or sub3 < 33):
    print("you are fail due less percentage in each subject by 33%")
elif(sub1+sub2+sub3)/3 < 40:
    print("you are fail due to total percentage less than 40")
else:
    print("congrat !\n you are passed!")
