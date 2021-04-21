#Program of bank class:
#**********************

class Account:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def __str__(self):
        return 'Account owner:{}\nAccount Balance: {}'.format(self.owner,self.balance)
    def deposit(self,amount):
        print('deposit of',amount,' is accepted')
        self.balance = self.balance + amount
        print('new balance after deposit:',self.balance)
        
    def withdraw(self,wamount):
        if wamount<self.balance:
            print(wamount, 'is withdrawn successfully!!')
            self.balance=self.balance-wamount
            print('Available balance after withdrawal:',self.balance)
        else:
            print( 'Funds Unavailable!')

'''
above __str__ is magic method, defined here because we want to print details
of object we have created, it won't be possible to print details of object
unless and untill __str__ method is overridden here (as print function
print whatever __str__ method returns). we can check that by
commenting the def __str__ code
'''


acct1=Account('abhi',200)
print(acct1.owner)
print(acct1.balance)
print(acct1)#to print this obj we have overridden str method

acct1.deposit(100)
acct1.withdraw(50)

print('\n')
acct2=Account('sukanya',100)
print(acct1.owner)
print(acct1.balance)
acct2.deposit(100)
acct2.withdraw(500)
