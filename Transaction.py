# To store transaction details

class Transaction:
    def __init__(self,sender,receiver,amount,time):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.time = time
    
    
    def getdata(self):
        return str(self.sender)+str(self.receiver)+str(self.amount)+str(self.time)
