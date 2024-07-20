from random import randint

class Train:

    def __init__(hoho,trainNo):
        hoho.trainNo = trainNo

    def book(hoho,fro,to):
        print(f"Ticket is booked in train no. : {hoho.trainNo} from {fro} to {to} ")

    def getStatus(hoho,):
        
        print(f"This Train({hoho.trainNo}) is running on time")

    def getFare(hoho,fro,to):
        print(f"Ticket is booked in train no. : {hoho.trainNo} from {fro} to {to} \n The ticket price is {randint(1000,3000)}")

t =Train(108108)
t.book("KhankiGiri","nangtobichi")
t.getStatus()
t.getFare("KhankiGiri","nangtobichi")