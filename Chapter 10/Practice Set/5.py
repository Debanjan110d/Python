from random import randint

class Train:

    def __init__(self,trainNo):
        self.trainNo = trainNo

    def book(self,fro,to):
        print(f"Ticket is booked in train no. : {self.trainNo} from {fro} to {to} ")

    def getStatus(self,):
        
        print(f"This Train({self.trainNo}) is running on time")

    def getFare(self,fro,to):
        print(f"Ticket is booked in train no. : {self.trainNo} from {fro} to {to} \n The ticket price is {randint(1000,3000)}")

t =Train(108108)
t.book("KhankiGiri","nangtobichi")
t.getStatus()
t.getFare("KhankiGiri","nangtobichi")