from abc import ABC,abstractmethod

class BankAccount(ABC):
    INTREST_RATE=0.04
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        self.transactions=[]
        self.transactions.append(f'Initial balance is {balance}')
        
    @abstractmethod
    def deposit(self,Amount):
        if Amount<0:
            raise ValueError('Amount should be greater than zero!!!')
        self.balance+=Amount
        self.transactions.append(f'Amount deposited is {Amount}')
    def withdraw(self,Amount):
        if self.balance<Amount:
            raise ValueError('Insufficient Fund!!')
        self.balance-=Amount
        self.transactions.append(f'Amount withdraw is {Amount}')
    def transfer(self,rev_account,Amount):
        self.withdraw(Amount)
        rev_account.deposit(Amount)
        self.transactions.append('Above The Amount transfered from your account')
        rev_account.transactions.append('Above Amount is transfered to your Account')
    def roi(self):
        intrest_amount=self.balance*self.__class__.INTREST_RATE
        self.deposit(intrest_amount)
        self.transactions.append('Above amount is created by INTREST_RATE')
    def statement(self):
        for transaction in self.transactions:
            print(transaction)
        print('*'*30)
        print(f'Total current balance is {self.balance}')
        
          

##c1=BankAccount('steve jobs',1000)
##c2=BankAccount('Bill gates',2000)
##c3=BankAccount('Tim cook',4000)
