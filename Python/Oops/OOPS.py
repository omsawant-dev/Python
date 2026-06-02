##class Point:
##    a=1
##    b=2
##    def add(x,y):
##        return x+y
##
##p1=Point()
##p2=Point()

##class Bank:
##    bname='SBI'
##    mbl='mumbai'
##    ceo='Mr.Yash'
##
##c1=Bank()
##c1.name='steve'
##c1.account_num='SBI65577889'
##c1.balance=20000
##
##c2=Bank()
##c1.name='bill'
##c1.account_num='SBI65577890'
##c1.balance=30000
##
##c3=Bank()

##Create a class with 5 class members and 5 object members and minimum 4 objects .
##class School:
##    sname='DAV'
##    smobile='022-256789'
##    sadd='Airoli'
##    sprincipal='Rajiv'
##    smanagement='DAVmanagement'
##
##s1=School()
##s1.name='Om'
##s1.roll=36
##s1.mobile=998877665544
##s1.add='Mulund'
##s1.div='B'
##
##s2=School()
##s2.name='Advik'
##s2.roll=21
##s2.mobile=9987654321
##s2.add='Mulund'
##s2.div='B'
##
##s3=School()
##s3.name='Sam'
##s3.roll=28
##s3.mobile=912234455566
##s3.add='Mulund'
##s3.div='B'
##
##s4=School()
##s4.name='Jordan'
##s4.roll=30
##s4.mobile=99887345677
##s4.add='Mulund'
##s4.div='B'
##    
##class Company:
##    ename='apple'
##    ceo='steve jobs'
##    mbl='california'
##    number_of_branches=100
##    number_of_emps=5000
##    def __init__(self,Id,name,ph_no,gmail,sal):
##        self.Id=Id
##        self.name=name
##        self.ph_no=ph_no
##        self.gmail=gmail
##        self.sal=sal
##
##e1=Company(101,'satish',8797895932,'sa@gmail.com',10000)
##e2=Company(102,'shaunak',8797845669,'sh@gmail.com',20000)
##e3=Company(103,'siddhesh',8797892332,'si@gmail.com',30000)
##e4=Company(104,'prathmesh',8797895324,'pr@gmail.com',40000)
##e5=Company(105,'om',87972142432,'om@gmail.com',50000)

##Company.__init__(e1,101,'satish',8797895932,'sa@gmail.com',10000)
##Company.__init__(e2,102,'shaunak',8797845669,'sh@gmail.com',20000)
##Company.__init__(e3,103,'siddhesh',8797892332,'si@gmail.com',30000)
##Company.__init__(e4,104,'prathmesh',8797895324,'pr@gmail.com',40000)
##Company.__init__(e5,105,'om',87972142432,'om@gmail.com',50000)



class BankAccount:
    INTREST_RATE=0.04
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        self.transactions=[]
        self.transactions.append(f'Initial balance is {balance}')
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

##Single Level Inheritence
class SavingAccount(BankAccount):
    INTREST_RATE=0.045
    def __init__(self,name,balance,phone_number):
        super().__init__(name,balance)##        BankAccount.__init__(self,name,balance)
        self.phone_number=phone_number
    def withdraw(self,Amount):
        if Amount<100:
            raise ValueError("You can not withdraw amount less than 100rs.")
        super().withdraw(Amount)

##c4=SavingAccount('Rolex',4000,9874561233)

##Multi Level Inheritence
class SalaryAccount(SavingAccount):
    INTREST_RATE=0.05
    def __init__(self,name,balance,phone_number,comp_name):
        super().__init__(name,balance,phone_number)
        self.comp_name=comp_name

##c5=SalaryAccount('Om',100000,8369347244,'apple')


##Multiple Inhertience
class Object:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        self.transactions=[]
        self.transactions.append(f'Initial balance is {balance}')
    

class Transaction:
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



class Other_Transaction:
    def roi(self):
        intrest_amount=self.balance*self.__class__.INTREST_RATE
        self.deposit(intrest_amount)
        self.transactions.append('Above amount is created by INTREST_RATE')
    def statement(self):
        for transaction in self.transactions:
            print(transaction)
        print('*'*30)
        print(f'Total current balance is {self.balance}')

class Om_Account(Object,Transaction,Other_Transaction):
    INTREST_RATE=0.9


c6=Om_Account('Om',1000000000000000)

##Hierarchical Inheritence
class SBI_BankAccount(BankAccount):
    INTREST_RATE=0.04
   
c1=SBI_BankAccount('Sumit',10000)

class HDFC_BankAccount(BankAccount):
    INTREST_RATE=0.045
    
c2=HDFC_BankAccount('Malhar',10000)

class ICICI_BankAccount(BankAccount):
    INTREST_RATE=0.05
 
c3=ICICI_BankAccount('Kshitij',10000)

class Abhyudaya_BankAccount(BankAccount):
    INTREST_RATE=0.09
   
c4=Abhyudaya_BankAccount('Om',10000)

##Hybrid Inheritence
class Grandfather():
    def land(self):
        print('I own 10 acres of land')

class Dad(Grandfather): 
    def car(self):
        print('I can drive the car')
    def rules(self):
        print('ask your mom')

class Mom():
    def cook(self):
        print('I can cook food')
    def rules(self):
        print('Come home before 9pm')

class Son(Dad,Mom):    
    def mobile(self):
        print('I can use the mobile ')

s=Son()
    
##method overriding
class Calculator:
    def add(self,a,b):
        return a+b
    def add(self,a,b,c):
        return a+b+c
u1=Calculator()
u2=Calculator()

##print(u1.add(1,2))
##print(u2.add(1,2,3)) 

##Polymorphism
##method overloading
class Calculator:
    def add(self,a=0,b=0,c=0,d=0):
        return a+b+c+d

##operator overloading
##class Point:
##    def __init__(self,x):
##        self.x=x
##    def __add__(self,other):
##        return self.x+other.x
##    def __sub__(self,other):
##        return self.x-other.x
##
##p1=Point(10)
##p2=Point(20)
##
##Access specifier Public,Protected and private
##class Point:
##    a=10
##    _b=20
##    __c=30
##    def __init__(self,x):
##        self.x=x
##    def __add__(self,other):
##        return self.x+other.x
##    def __sub__(self,other):
##        return self.x-other.x
##
##p1=Point(10)
##p2=Point(20)
##
##print(p1.a)
##print(p1._b)
##print(p1.__c)


class BankAccount:
    INTREST_RATE=0.04
    def __init__(self,name,balance,Acc_num):
        self.name=name
        self.__balance=balance
        self.Acc_num=Acc_num
        
    def get_balance(self):
        acc_num=input("Enter the account number :")
        if self.Acc_num!=acc_num:
            raise ValueError('Wrong Account Number')
        return self.__balance

    def set_balance(self,Amount):
        acc_num=input("Enter the account number :")
        if self.Acc_num!=acc_num:
            raise ValueError('Wrong Account Number')
        self.__balance+=Amount

##c1=BankAccount('steve jobs',1000,'SBI123')
##c2=BankAccount('tim cook',2000,'SBI456')
##c3=BankAccount('om',9999999999,'SBI789')
            
class BankAccount:
    INTREST_RATE=0.04
    def __init__(self,name,balance,Acc_num):
        self.name=name
        self.__balance=balance
        self.Acc_num=Acc_num
        
    def get_balance(self):
        acc_num=input("Enter the account number :")
        if self.Acc_num!=acc_num:
            raise ValueError('Wrong Account Number')
        return self.__balance

    def set_balance(self,Amount):
        acc_num=input("Enter the account number :")
        if self.Acc_num!=acc_num:
            raise ValueError('Wrong Account Number')
        self.__balance+=Amount
    balance=property(get_balance,set_balance)


class BankAccount:
    INTREST_RATE=0.04
    def __init__(self,name,balance,Acc_num):
        self.name=name
        self.__balance=balance
        self.Acc_num=Acc_num
    @property   
    def balance(self):
        acc_num=input("Enter the account number :")
        if self.Acc_num!=acc_num:
            raise ValueError('Wrong Account Number')
        return self.__balance
    @balance.setter
    def balance(self,Amount):
        acc_num=input("Enter the account number :")
        if self.Acc_num!=acc_num:
            raise ValueError('Wrong Account Number')
        self.__balance+=Amount
    

##c1=BankAccount('steve jobs',1000,'SBI123')
##c2=BankAccount('tim cook',2000,'SBI456')
##c3=BankAccount('om',9999999999,'SBI789')

        
####User Defined Error
##class PasswordError(Exception):
##    pass
##
##pwd='py@123'
##password=input("Enter the password :")
##if password==pwd:
##    print("Login Successful")
##else:
##    raise PasswordError("Wrong Password")

a=10
b=12.5
st='apple'
lst=[10,20,30,40]
tp=(1,2,3)
s={4,5,6}
d={'a':1,'b':2,'c':3}
r=range(1,6)
z=zip('abc',[2,4,6,8])
e=enumerate("YASH")
    
for ll 
