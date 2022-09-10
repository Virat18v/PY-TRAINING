# a function to find whether a seat is available or not
class Train:
    def __init__(self , name , fare , seats):
         self.name = name
         self.fare = fare
         self.seats = seats
         
    def getStatus(self):
        print("*************")
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train are {self.seats}")

    
    def fairinfo(self):
        print(f"The price of the ticket is: Rs {self.fair}")        
        
    def bookticket(self):
        if(self.seats>0):
            print(f"your ticket has been booked your ticket no is : {self.seats}")         
            self.seats = self.seats -1
        else:
            print("sorry for inconvenience,The train is currently full kindly go for tatkal")
    
janhit = Train("Janhit Express: 14921",90,3)     
janhit.getStatus()
janhit.bookticket()
janhit.getStatus()
#if the availability of seat is 3
janhit.getStatus()
        