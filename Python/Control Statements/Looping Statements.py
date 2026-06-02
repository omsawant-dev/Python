##While Loop
##1.WAPT print given list into 5 times.
##list=[10,20,30,40]
##i=1
##while i<=5:
##    print(list)


##2. WAPT print number from 0-9
##i=0
##while i<=9:
##    print(i)
##    i+=1

##3. WAPT print all the even numbers between the range 1 to 100.
##i=1
##while i<=100:
##    if i%2==0:
##        print(i)
##    i+=1

##i=2
##while i<=100:
##    print(i)
##    i+=2

##4.WAP to print multiplication tables of given numbers, take input from user.
##num=int(input("Enter the number for table :"))
##i=1
##while i<=10:
##    print(f"{num}*{i}={num*i}")
##    i+=1


##5.WAP to find sum of 'n' natural numbers.
##n=int(input("Enter the 'n' number :"))
##i=1
##Sum=0
##while i<=n:
##    Sum=Sum+i
##    i+=1
##print(f"Sum of n natural number is : {Sum}")


##6.WAP to print one by one char from given name.
##name=input("Enter the name :")
##l=len(name)-1
##i=0
##while i<=l:
##    print(name[i])
##    i+=1


##7.WAP to print elements of list are Even or odd.
##lst=[22,43,56,35,98,67,52]
##i=0
##while i<len(lst):
##    if lst[i]%2==0:
##        print(f"Number is Even ie {lst[i]}")
##    else:
##        print(f"Number is Odd ie {lst[i]}")
##    i+=1


##7.WAP to print even numbers from 0 to 20 in a single line.
##i=2
##lst=[]
##while i<=20:
##    lst.append(i)
##    i+=2
##print(lst) # question doesnot require number in list

##i=0
##while i<=20:
##    print(i,end=' ')
##    i+=2

##8.WAP to check given number is palindrome or not.
##num=int(input("Enter the number :"))
##a=int(input("Enter the number :"))
##b=str(a)
##i=0
##j=len(b)-1
##while i<len(b):
##    if b[i]==b[j]:
##        i+=1
##        j-=1
##        
##    else:
##        print("Not a palindrome")
##        break
##    
##print("Palindrome")

##without while loop
##a=121
##
##if str(a)==str(a)[::-1]:
##    print("Yes it is a palindrome")
##else:
##    print("No it is not a palindrome")

##9. WAP to check given number is palindrome or not without typecasting.
##num=int(input("Enter the number :"))
##rev=0
##i=num
##while i!=0:
##    last_digit=i%10
##    rev=rev*10+last_digit
##    i=i//10
##if num==rev:
##    print("Yes it is a palindrome")
##else:
##    print("No it is not a palindrome")


##10.WAP to print sum of the numbers by taking start and end from user
##start=int(input("Enter the start number :"))
##end=int(input("Enter the end number :"))
##Sum=0
##while start<=end:
##    Sum=Sum+start
##    start+=1
##print(Sum)

##11. WAP to print sum of all the numbers present in a list.
##lst=[22,54,76,87,64,42,97,65]
##i=0
##Sum=0
##while i<len(lst):
##    Sum=Sum+lst[i]
##    i+=1
##print(Sum)

##12.WAP to extract all the vowels and digit from the given string.
##st='Happy Gudi padva 2026 3 19'
##i=0
##vowel_digit=''
##while i<len(st):
##    if st[i] in 'AEIOUaeiou' or st[i].isdigit():
##        vowel_digit=vowel_digit+st[i]
##    i+=1
##print(vowel_digit)


##13.WAP to extract tuple of all the string data from given tuple
##data=('steve jobs',101,5.8,'bill gates',102,6.0,'Tim cook',103,5.2)
##i=0
##name=()
##while i<len(data):
##    if type(data[i])==str:
##        name=name+(data[i],)
##    i+=1
##
##print(name)

##For Loop
##1.WAP to execute all the uppercase vowel present inside the given string.
##st='YAlleShA ROcKY'
##vowels=''
##
##for i in st :
##    if i in 'AEIOU':
##        vowels+=i
##print(vowels)


##2.WAP to find length of given collection without using len function.
##data=eval(input("Enter the data :"))
##count=0
##for i in data:
##    count=count+1
##print(count)


##3.WAP to extract all the uppercase and lowercase and digit and special symbols, separately from given string.
##st='YAlleSH@19$'
##upper=''
##lower=''
##digit=''
##special=''
##for i in st:
##    if i.isupper():
##        upper=upper+i
##    elif i.islower():
##        lower+=i
##    elif i.isdigit():
##        digit+=i
##    else:
##        special+=i
##print(upper,lower,digit,special)

##4.WAP to count the specified character from the given string without using count method.
##st='Hello World'
##char='l'
##count=0
##for ch in st:
##    if char==ch:
##        count=count+1
##
##print(count)
        

##5.WAP to print numbers from 1 to 10 using while and wap to print numbers from 1 to 10 using for loop.
##i=1
##while i<=10:
##    print(i)
##    i+=1
##
##for i in range(1,11):
##    print(i)



## 6.WAP TO FIND THE FACTORIAL OF A GIVEN NO.
##num=int(input("Enter the number :"))
##fact=1
##for i in range(num,0,-1):
##    fact=fact*i
##print(fact)


##7.WAP to print the divisible of given number , ie ,6=1,2,3,6
##num=int(input("Enter the number :"))
##for i in range(1,num+1):
##    if num%i==0:
##        print(i)


##8.WAP to print sum of the divisible number excluding that number.
##num=int(input("Enter the number :"))
##Sum=0
##for i in range(1,num):
##    if num%i==0:
##        Sum=Sum+i
##print(Sum)


##9.WAP to check whether given number is perfect number or not.(IMP)
##num=int(input("Enter the number :"))
##Sum=0
##for i in range(1,num):
##    if num%i==0:
##        Sum=Sum+i
##if Sum==num:
##    print("it is a perfect number")
##else:
##    print("it is not a perfect number")
##print(Sum)


##10.WAP to print multiplication table for any number.
##num=int(input("Enter the number :"))
##for i in range(1,11):
##    print(f"{num} * {i} = {num*i}")


##11.WAP to print sum of n natural numbers.
##num=int(input("Enter the number :"))
##Sum=0
##for i in range(1,num+1):
##    Sum=Sum + i
##print(f"Sum of n natural number is {Sum}")


##12.WAP to get sum of all integer number present inside the list.
##lst=eval(input("Enter the list :"))
##Sum=0
##for i in range(0,len(lst)):
##    if type(lst[i])==int:
##        Sum=Sum+lst[i]
##
##print(f"Sum of all the int num inside list is {Sum}")


##13.WAP to reverse the string without using built in function.
##data=input("Enter the data :")
##rev=''
##for i in range(len(data)-1,-1,-1):
##    rev=rev+data[i]
##print(rev)

##data=input("Enter the data :")
##rev=''
##for char in data:
##    rev=char+rev
##print(rev)


##14.Wap to get the following output
##Input='hello'
##Output={}
####output={0:'h',1:'e',2:'l',3:'l',4:'o'}
##for i in range(0,len(Input)):
##    value=Input[i]
##    Output[i]=value
##print(Output)

##st='hello'
##Dict={}
##for i in range (0,len(st)):
##    Dict[i]=st[i]
##print(Dict)


##15.WAP to get following output
##Input=['hai','hello','how','are','you']
##output={'hai':3,'hello':5,'how':3,'are':3,'you':3}
##Output={}
##for i in range(0,len(Input)):
##    key=Input[i]
##    value=len(Input[i])
##    Output[key]=value
##print(Output)


##lst=['hai','hello','how','are','you']
###output={'hai':3,'hello':5,'how':3,'are':3,'you':3}
##Dict={}
####for i in range(0,len(lst)):
####    Dict[lst[i]]=len(lst[i])
####print(Dict)
##
###easy way without using range
##for i in lst:
##    Dict[i]=len(i)
##print(Dict)

##16.WAP uppercase Alphabhet from A-Z using while and for loop.
##i=ord('A')
##char=''
##while i<=ord('Z'):
##    char=char+chr(i)
##    i+=1
##print(char)

##for Ascii in range(ord('A'),ord('Z')+1):
##    print(chr(Ascii))

###continue
##i=ord('A')
##char=''
##while i<=ord('Z'):
##    if chr(i) in 'AEIOU':
##        continue
##    char=char+chr(i)
##    i+=1
##print(char)
##
###break
##char=input("Enter Stop char :")
##for Ascii in range(ord('A'),ord('Z')+1):
##    if char==chr(Ascii):
##        break
##    print(chr(Ascii))


##break
##1.WAP to print only first uppercase character from given string name='yALLUsH'
##name='yALLUsH'
##for i in name:
##    print(i)
        

##2.WAP to print smallest divisor of given number other than 1.
##num=int(input("Enter the number :"))
##for i in range(2,num+1):
##    if num%i==0:
##        print(i)
##        break

##3.WAP to print the initial index of a given character present inside the given string.
##st='hello'
##char='l'
##for i in range(0,len(st)):
##    for char in st:
##        if char==st:
##            print(i)
##            break


##1.WAP to run the loop continuesly untill user enter proper password.
##saved_pwd='Pysp112'
##while True:
##    pwd=input("Enter the password: ")
##    if saved_pwd==pwd:
##        print("Login Successfully")
##        break
##    else:
##        print("Wrong Password")


##2.WAP to guess the number .
##n=45
##count=0
##while True:
##    num=int(input("Enter the number :"))
##    if n==num:
##        print("Congrats you have enter right number")
##        count+=1
##        break
##    elif n>num:
##        print("Increase the number")
##        count+=1
##    else:
##        print("Decrease the number")
##        count+=1
##print(f"You have guessed the number in {count} guesses")

#Nested For loop
##1.WAP to access characters one by one from all the string which are present inside 
##lst=['TCS','IBM','EY']
##for char in lst:
##    for i in char:
##        print(i)

##2.WAP to get the following output
##Input=[12,'hai',89,'executed',6.7,'python']
##Output={'hai':2,'executed':4,'python':1}
##word_vowel={}
##
##for value in Input:
##    if type(value)==str:
##        count=0
##        for char in value:
##            if char in 'AEIOUaeiou':
##                count+=1
##        word_vowel[value]=count
##print(word_vowel)

##3.WAP to get the following output without using slicing
##Input=[12,'hai',89,'program',6.7,'python']
####Output={'margorp', 6.7, 12, 89, 'nohtyp', 'iah'}
##S=set()
##rev=''
##for value in Input:
##    if type(value)==str:
##        rev=''
##        for char in value:
##            rev=char+rev
##        S.add(rev)
##    else:    
##        S.add(value)  
##print(S)

##4.WAP to get the following output without using len.
##st='python is very easy'
##D={}
##for word in st.split():
##    count=0
##    for char in word:
##        count+=1
##    D[word]=count
##print(D)



        






        
