##x=10
##def outer():
##    global x
##    x=x+1
##    print(x)
##outer()
##print(x)

##1.Implement a func it should return sum of minimum 3 no and maximum 5 no
##def Sum(a,b,c,d=0,e=0):
##    return a+b+c+d+e
##print(Sum(1,2,3,8,9))


##2. Write a function to get product of minimum 2no and maximum 5 no.
##def Product(a,b,c=1,d=1,e=1):
##    return a*b*c*d*e
##print(Product(2,3))
##print(Product(2,3,4))
##print(Product(2,3,5,5))
##print(Product(2,3,5,6,7))

##Argument Restriction
##Positional Argument
##def add(a,b,c,/):  
##    print(a,b,c)
##    return a+b+c
##
##print(add(1,2,3))

##Keyword Argument
##def add(*,a,b,c):
##    print(a,b,c)
##    return a+b+c
##
##print(add(a=1,c=2,b=3))

##Combiantion Argument
##note: / should be ahead of *
##def add(a,/,b,*,c): a is positional arg , c is keyword arg and b can be anything
##    print(a,b,c)
##    return a+b+c
##
##print(add(2,b=3,c=10))
##print(add(2,3,c=10))

##tuple packing or positional argument packing or single packing
##def pack(*args):
##    return (args)
##    
##print(pack())
##print(pack(1,2,3,4,4,5,5))
##print(pack('a',2,3,4))

##dict packing or keyword argument packing or double packing
##def pack(**kwargs):
##    return(kwargs)
##    
##print(pack())
##print(pack(a=1,b=3,c=5))
##print(pack(ID=101,name="OM",age=22,salary=123456789))

##combination (positional followed by keyword argument
##def pack(*args,**kwargs):
##    print(args)
##    print(kwargs)
##print(pack(1,2,3,a=1,b=0))


##1.Write a function to check a number given is even or not , if it is even return true or else false.
##num=int(input("Enter the number :"))
##
##def Even(num):
##    if num%2==0:
##        return True
##    return False
##
##print(Even(num))
##
####optimized way
##def Even(num):
##    return num%2==0
##
##print(Even(num))

##2.create a fun to check given word is palindrome or not.
##word=input("Enter the data :")
##def Palindrome(word):
##    return word==word[::-1]
##print(Palindrome(word))

##3. check whether the given word is captial or not without using method.
##word=input("Enter the data :")
##def Isupper(word):
##    return 'A'<=word<='Z'
##
##print(Isupper(word))

##4. create a func to print numbers from first argu to second argu.
##arg1=int(input("Enter the number :"))
##arg2=int(input("Enter the number :"))
##
##def numbers(arg1,arg2):
##    i=arg1
##    while i<=arg2:
##        print(i)
##        i+=1
##
##print(numbers(arg1,arg2))

##5.create a func to create a list of user enter number .
##num1=int(input("Enter the number :"))
##num2=int(input("Enter the number :"))
##
##def List(num1,num2):
##    l=[]
##    for i in range(num1,num2+1):
##        if i%2==0:
##            l.append(i)
##
##print(List(num1,num2))


##def List(num1,num2):
##    return [num for num in range(num1,num2) if num%2==0]
##print(List(num1,num2))

##6.waf to check given num is perfect number , prime number , armstrong number , peterson number
##or not
##def isperfect(num):
##    Sum=0
##    for i in range(1,num):
##        if num%i==0:
##            Sum+=1
##    return Sum==num
##print(isperect(num))
##
##def isprime(num):
##    count=0
##    for i in range(1,num+1):
##        if num%i==0:
##            count+=1
##    return count==2
##
##def isprime(num):
##    for i in range(1,num+1):
##        if num%i==0:
##            return False
##
##    return True
##
##print(isprime(10))

##def isArmstrong(num):
##    snum=str(num)
##    Sum=0
##    for digit in snum:
##        Sum+=int(digit)**len(snum)
##
##    return Sum==num
##
##print(isArmstrong(153))
##
##def ispeterson(num):
##    Sum=0
##    snum=str(num)
##    for digit in snum:
##        fact=1
##        for i in range(1,int(digit)+1):
##            fact*=i
##        Sum+=fact
##    return Sum==num
##
##print(ispeterson(145))

##def fact(digit):
##    fact=1
##    for i in range(1,digit+1):
##        fact*=i
##    return fact
##
##def ispeterson(num):
##    Sum=0
##    snum=str(num)
##    for digit in snum:
##        Sum+=fact(int(digit))
##    return Sum==num
##
##print(ispeterson(145))

##7.Wap numbers from 1 to 10 without using any loops.

##def loop(i=1):
##    if i<11:
##        print(i)
##        loop(i=i+1)
##    
##loop()

##8.Wap evens from 20 to 2 

##def even(i=20):
##    if i>=2:
##        print(i)
##        even(i=i-2)
##
##even()

##def even(i=20):
##    if i>=2:
##        if i%2==0:
##            print(i)
##        even(i=i-1)


##9.Wap to acess one by one char from string.
##team='RCB'
##char=''
##def index(st,i=0):
##    if i<len(st):
##        print(st[i])
##        index(st,i=i+1)
##
##index(team)

##10.Wap to acess data from given list even numbers.
##data=[1,2,3,4,5,1,2,3,4,5,6,7,8,9,4,10,20]
##
##def loop(data,lst=[],i=0):
##    if i<len(data):
##        if data[i]%2==0:
##            lst.append(data[i])
##        loop(data,lst,i=i+1)
##    return lst
##
##
##print(loop(data))

##11.Wap to get following output.
##Input=[12,'hai',89,'Executed',6.7,'python']
##Output={'hai':2,'Excuted':4,'python':1}
##
##def word_vowel(lst,i=0,j=0):
##    if i<len(lst):
##        count=0
##        if type(lst[i])==str:
##            if j<len(lst


##
##def chars(names,i=0,j=0):
##    if i<len(names):
##        if j<len(names[i]):
##            print(names[i][j])
##            chars(names,i,j=j+1)
##        else:
##            chars(names,i=i+1,j=0)
##
##chars(['YASH','RAM','KASHI','PAWAN'])

##12.wap to extract string data from the tuple.
##numbers=('apple',12,4.5,'google',(2+4j),'tcs')
##l=[]
##def extract(numbers,i=0):
##    if i<len(numbers):
##        if type(numbers[i])==str:
##            l.append(numbers[i])
##        extract(numbers,i=i+1)
##extract(numbers)
##print(l)
##data=('apple',12,4.5,'google',(2+4j),'tcs')
##def str_data(data,out=[],i=0):
##    if i==len(data):
##        return out
##    if type(data[i])==str:
##        out.append(data[i])
##    return str_data(data,out,i=i+1)
##    
##print(str_data(data))

##13.Wap to find factorial of any number using recursion.
##def factorial(num):
##    if num==0 or num==1:
##        return 1
##    return num*factorial(num-1)
##
##print(factorial(3))

##11. Wap to extract all the vowels from the str using recursion.
##st='Hello World hi python'
##def string(st,out='',i=0):
##    if i<len(st):
##        if st[i] in 'AEIOUaeiou':
##            out=out+st[i]
##        return string(st,out,i=i+1)
##    return out
##print(string(st))


##data=[12,'hai',89,'excuted',6.7,'python']
##def dvc(data,out={},i=0,j=0,count=0):
##    if i>=len(data):
##        return out
##    if type(data[i])==str:
##        if j<len(data):
##            if data[i][j] in 'AEIOUaeiou':
##                count+=1
##            return dvc(data,out,i,j+1,count)
##        else:
##            out[data[i]]=count
##            return dvc(data,out,i+1,0,0)
##
##    else:
##        return dvc(data,out,i+1,0,0)
##
##print(dvc(data))
        
    
##a=10
##b=20.5
##lst=[10,20,30]
##d={'a':1,'b':2}
##from time import sleep
##def display(func_add,*args,**kwargs):
##    sleep(2)
##    return func_add(*args,**kwargs)
##
##def greet():
##    return "Hello World"
##def greeting(name):
##    return f"Hello {name}"
##def add(a,b):
##    return a+b
##def mul(a,b,c):
##    return a*b*c
##
##print(display(add,10,30))
##print(display(mul,10,30,40))
##print(display(greet))
##print(display(greeting,'om'))

##a=10
##b=20.5
##lst=[10,20,30]
##d={'a':1,'b':2}
from time import sleep
def delay(func_add):
    def wrapper(*args,**kwargs):
        sleep(2)
        return func_add(*args,**kwargs)
    return wrapper
@delay
def greet(): #greet==>delay(greet)===>wrapper
    return "Hello World"
@delay
def greeting(name):#greet==>delay(greeting)===>wrapper
    return f"Hello {name}"
@delay
def add(a,b):
    return a+b
@delay
def mul(a,b,c):
    return a*b*c


##implement the log message decorator or create a func it should add good evening to all other functions before the result



