# creating a class programmer for information
class Programmer:
    company = "google"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"The name of the {self.company} programmer is {self.name} and the product is {self.product}")


harry = Programmer("virat", "Skype")
alka = Programmer("vishal", "GitHub")
harry.getInfo()
alka.getInfo()