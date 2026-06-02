from time import sleep
##def display():
##    print("Hi")
##    yield 1
##    print('Every')
##    yield 2
##    print('One')
##    yield 3
##    print('Welcome')
##
##gen=display()
##for i in gen:
##    print(i)
##    sleep(1)


#WAP to generate even number from 1 to 100.
##r=range(2,101,2)
##for i in r:
##    print(i)

##def even_num():
##    i=1
##    while i<=100:
##        if i%2==0:
##            yield i
##        i+=1
##nums=even_num()
##print(list(nums))

##Wap to generate infinite odd numbers from 1.
##def odd_num():
##    i=1
##    while True:
##        yield i
##    i+=2
##odd=odd_num()
##for i in odd:
##    print(i)
##    sleep(1)


##Wap to generate perfect number series.
##def perfect():
##    num=1
##    while True:
##        Sum=0
##        for i in range(1,num):
##            if num%i==0:
##                Sum=Sum+i
##        if Sum==num:
##            yield num
##        num+=1
##for i in perfect():
##    print(i)

##Wap to generate the prime number series
##def prime():
##    num=2
##    while True:
##        Count=0
##        for i in range(1,num+1):
##            if num%i==0:
##                Count+=1
##        if Count==2:
##            yield num
##        num+=1
##
##for i in prime():
##    print(i)
##    sleep(2)
##
##def prime():
##    num=2
##    while True:
##        isprime=True
##        for i in range(1,num+1):
##            if num%i==0:
##                isprime=False
##        if isprime:
##            yield num
##        num+=1
##
##for i in prime():
##    print(i)
##    sleep(2)


##Note for mock sir will ask one fix question about number question (armstrong , perfect , prime , sum of first five, etc)
##Wap to generate armstrong , fibonicci, palindrome number without using typecasting series.

##Armstrong
##def armstrong():
##    num=1
##    while True:
##        Sum=0
##        digits=str(num)
##        for digit in digits:
##            Sum+=int(digit)**len(digits)
##        if Sum==num:
##            yield num
##        num+=1
##
##for i in armstrong():
##    print(i)
##    sleep(1)

##Palindrome
##def palindrome():
##    num=1
##    while True:
##        n=num
##        rev=0
##        while n!=0:
##            last_digit=n%10
##            rev=rev*10+last_digit
##            n=n//10
##        if num==rev:
##            yield num
##        num+=1
##
##
##for i in palindrome():
##    print(i)
##    sleep(1)


##Fibonicci
##def fibonicci():
##    a,b=0,1
##    while True:
##        yield a
##        a,b=b,a+b
##
##
##for i in fibonicci():
##    print(i)
##    sleep(1)


##wap to get list of squares of numbers which are present inside given list usinf while loop,using for loop and
##comphrension, recursion,generator.

lst=[1,2,3,4,5]
i=0
##while i<len(lst):
##    print(lst[i]**2)
##    i+=1
    

##for i in lst:
##    print(lst[i]**2)
    
##print([ lst[i]**2 for i in lst )])

##def square():
##    i=0
##    while i<=len(lst)-1:
##        yield lst[i]**2
##        i+=1
##    
##for i in square():
##    print(i)
##    sleep(1)


##def Square(lst,out=[],i=0):
##    if i<len(lst):
##        out.append(lst[i]**2)
##        Square(lst,out,i=i+1)
##    return out
##
##print(Square([1,2,3,4,5]))
##


##Generator expression
##print(list(v**2 for v in lst))

##Generator expression
##wap to filter the even numbers
##numbers=[1,18,2,45,3,10,4,12,5,7,6,7,8,9,10,333,17]
##print(list(e for e in numbers if e%2==0))


##Lambda
## func_name = lambda args: expression or result of function
##wap to generate given number is even or not, if it is even return True else False.
##def even(num):
##    return num%2==0

##even = lambda num : num%2==0
##print(even(4))
##print(even(5))



##add = lambda num : num+15
##print(add(10))
##
##square = lambda num : num**2
##cube = lambda num : num**3
##sq_cu = lambda num : (num**2,num**3)
##
##addtwo = lambda num1,num2 : num1+num2
##
##exp1 = lambda a,b : a**2 + b**2 + 2*a*b
##
##exp2 = lambda a,b,c : 2*a + 3*b + 4*c
##
##last = lambda a : a[-1]
##
##check = lambda a : a%2==0
##
##palindrome = lambda a : a=a[::-1]
##
##pos = lambda a : a*-1 if a<0 else a
##pos = lambda a : abs(a)
##
##present = lambda ch,st : ch in st

##Map
##Wap to square every number in a given list of integers
##print(list(map(lambda num : num**2 , [1,2,3,4,5])))

##Wap to find if given squence starts with 'a'.
##name = ['Anna', 'Bob']
##print(list(map(lambda st : st[0]=='A' , name)))


##wap to print tuple of length of each and every name present inside the given list of the name.
##name=["Alex","Steve Jobs","Anna","Henry", "John"]
##print(tuple(map(lambda a : len(a) , name)))
##print(tuple(map(len,name)))

##Wap to convert negative numbers in a given list to positive num.
##nums=[1,-8,-3,4,-7,-12]
##print(list(map(lambda a : abs(a) , nums)))
##print(list(map(abs,name)))

##Wap to return a list of elements raised to the power of their indices.
##lst=[1,2,3,4,5]
##print(list(map(lambda value: value[1]**value[0] , enumerate(lst))))

##filter
##Wap to extract all the positive numbers only from the list .
##nums=[1,-8,-3,4,-7,-12,18]
####print(list(map(lambda num : num>=0 , nums)))
####print(list(filter(lambda num : num>=0 , nums)))

####Wap to calculate the sum of only positive numbers.
##nums=[1,-8,-3,4,-7,-12,18]
##print(sum(filter(lambda num : num>=0 , nums)))

##Wap to print set of only even numbers in the range 1-50.
print(set(filter(lambda n : n%2==0 , range(1,50))))

##build a list with only even length string using filter class.
names = ['apple','google','yahoo','facebook','yelp','flipkart','gmail','instagram','microsoft']
print(list(filter(lambda st : len(st)%2==0,names)))


##Return the string if the string is starting from vowel character.
names=['laura','steve','bill','james','bob','greg','scott','alex','ive']
print(list(filter(lambda st : st[0] in 'AEIOUaeiou' ,names)))

##
print(sum(map(int,(lambda char:char.isdigit(),st))))







    
