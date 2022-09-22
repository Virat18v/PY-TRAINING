class employee:
    comany = "amazon"

    def showdetails1(self):
        print("This is an employee of comapany")

    def showdetails2(self):
        print("Indian")

    def showdetails3(self):
        print("cricket-player")

    def showdetails4(self):
        print("founder of vidyayan")


class programmer(employee):
    language1 = "English"
    language2 = "French"

    def getlanguage2(self):
        print(f"The language is {self.language2}")

    def showdetails2(self):
        print("this is an employee of company")


# I want to know 2nd details of an employee
e = employee()
e.showdetails1()
e.showdetails2()
e.showdetails3()
e.showdetails4()
# I WANT TO GET 2ND LANGUAGE OF THE PROGRAMMER

p = programmer()
p.getlanguage2()

print("********THANK-YOU**********")
