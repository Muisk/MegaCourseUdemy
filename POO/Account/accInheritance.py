class Account:

    def __init__(self,filepath):
        self.filepath=filepath
        with open(filepath,'r')as file:
            self.balance=int(file.read())
    
    def withdraw(self,amount):
        self.balance=self.balance - amount
        
    def deposit(self,amount):
        self.balance=self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

class Checking(Account):
    """This class generates checking accounts objects"""
    type="checking"
    def __init__(self,filepath,fee):
        Account.__init__(self,filepath)
        self.fee=fee
    
    def transfer(self,amount):
        self.balance=self.balance-amount-self.fee

diego_checking=Checking("DiegoBalance.txt",1)
diego_checking.transfer(10)
print(diego_checking.balance)
diego_checking.commit()
print(diego_checking.type)

nico_checking=Checking("NicoBalance.txt",1)
nico_checking.transfer(10)
print(nico_checking.balance)
nico_checking.commit()
print(nico_checking.type)

print(diego_checking.__doc__)