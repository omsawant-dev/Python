from Bank import BankAccount

class SavingAccount(BankAccount):
    INTREST_RATE=0.045
    def __init__(self,name,balance,phone_number):
        super().__init__(name,balance)##        BankAccount.__init__(self,name,balance)
        self.phone_number=phone_number
    def withdraw(self,Amount):
        if Amount<100:
            raise ValueError("You can not withdraw amount less than 100rs.")
        super().withdraw(Amount)
    def deposit(self,Amount):
        pass

c4=SavingAccount('Rolex',4000,9874561233)

print(c4.balance)
c4.deposit(4000)
print(c4.balance)


