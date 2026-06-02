##1.WAP to print list of numbers from 1 to 20.
##L=[]
##for i in range(1,21):
##    L.append(i)
##print(L)

##L=[]
##i=1
##while i<=20:
##    L.append(i)
##    i+=1
##print(L)

##L=[i for i in range(1,21)]
##print(L)

##2.WAP list of character in given string.
##greet='Hello world'
##print([char for char in greet])

##3.WAP list of square number which are present in given list
##numbers=[1,2,3,4,5]
##print([number**2 for number in numbers])

##4.Building a list of first_name and last_name from full_name
##full_names=["steve jobs","bill gates","john doe","tim cook"]
##first_name=[name.split()[0] for name in full_names]
##last_name=[name.split()[1] for name in full_names]
##
##print(first_name)
##print(last_name)

##5.WAP to print list of even numbers from 1 to 20
##print([num for num in range(1,21) if num%2==0])

##6.WAP TO PRINT PALINDROME FROM GIVEN LIST.
##names=['steve','eve','john','anna','stella','bob']
####pal=[]
####for i in names:
####    if i==i[::-1]:
####        pal.append(i)
####
####print(pal)

##print([i for i in names if i==i[::-1]])

##7.WAP to filter out those names which are less than 6 character
##names=['apple','google','yahoo','gmail','flipkart','instagram','microsoft']
####for i in names:
####    if len(i)<6:
####        print(i)
##
##print([i for i in names if len(i)<6])


##8.
##print([language for  language in languages if language[0]=='P'])
##
####9.
##print([name for name in names if len(name)%2==0])
##
####10.
##print([name[::-1] if len(name)%2!=0 else name for name in names])
##
####11.
##print([value[::-1] if type(value)==str else value for value in values ])

##12.
##a=[1,2,3,4]
##b=[5,6,7,8]
##sum_values=[]
##for i in range(len(a)):
##    sum_values.append(a[i]+b[i])
##print(sum_values[1])
##
##print([a[i]+b[i] for i in range(len(a))])

##13.using zip
##a=[1,2,3,4]
##b=[5,6,7,8]
####sum_values=[]
####for i,j in zip(a,b):
####    print(i+j)
##
##print([i+j for i,j in zip(a,b)])

##14.Raise to the power of list values based on its index position.
##lst=[1,2,3,4,5]
##for i in range(len(lst)):
##    print(lst[i]**i)
##
##print([lst[i]**i for i in range(len(lst))])
##
####using enumerate
##out=[]
##for index,value in enumerate(lst):
##    out.append(value**index)
##print(out)
##
##print([value**index for index,value in enumerate(lst)])


##2.SET COMPREHENSION
##1.WAP to extract set of unique and even numbers from given tuple of numbers.
##numbers=(1,2,3,4,1,2,3,41,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7)
##unique_even=set()
##for number in numbers:
##    if number%2==0:
##        unique_even.add(number)
##print(unique_even)
##        
##        
##print({item for item in numbers if item%2==0})
    
##2.WAP try same program as list comprehension

##3.Dictionary Comprehension
##1.WAP to build a dict of word and length pair
##sentence="This is a bunch of words"
##
##D={}
##for word in sentence.split():
##    D[word]=len(word)
##print(D)
##
##print({word:len(word) for word in sentence.split()})


##2.WAP flip key and values of the dict using dict comprehension.
##d={'a':1,'b':2,'c':3,'d':4}
##flip_d={}
##for key in d:
##    flip_d[d[key]]=key
##
##print(flip_d)
##print({d[key]:key for key in d })
##
##for k,v in d.items():
##    flip_d[v]=k
##print(flip_d)
##print({v:k for k,v in d.items()})

##3.WAP to count the number of each character in a string.
##sentence="hello world welcome to python hello hi world welcome to python"
##D={}
##for word in sentence.split():
##    D[word]=sentence.count(word)
##print(D)    
##print({char:sentence.count(char) for char in sentence.split()})

##c={}
##for char in sentence:
##    c[char]=sentence.count(char)
##print(c)
##print({char:sentence.count(char) for char in sentence})

##4.WAP to create dict of char and its ascii value pair
##s= 'abcABC'
##D={}
##for char in s:
##    D[char]=ord(char)
##print(D)
##print({char:ord(char) for char in s})

##5.create a dict building its height from given meter to feet
## 1 meter = 3.28 feet
##buildings={'burj khalifa':828 ,'shanghai tower':632,'abraj al bait clock tower':601,'ping an finance centre shenzhen':599,
##           'lotte world tower':554.5,'world trade center':541.3}
##D={}
##for k,v in buildings.items():
##    D[k]=v*3.28
##print(D)
##print({k:v*3.28 for k,v in buildings.items()})

##6.Creating dictionary of city and population pairs using dict comphrension.
##cities=['Tokyo','Delhi','Shanghai','Sao Paulo','Mumbai']
##population=['38,001,000','25,703,168','23,740,778','21,066,245','21,042,538']
##D={}
####for k in cities:
####    for v in population:
####        if cities[k]==population[v]:
####            print(k,v)
##
##for i in range(len(cities)):
##    for j in range(len(population)):
##        if i==j:
####            print(cities[i],population[j])
##            D[cities[i]]=population[j]
##print(D)
##print({cities[i]:population[j] for i in range(len(cities)) for j in range(len(population)) if i==j})
##print({city:popu for city,popu in zip(cities,population)})

####7.Building a dictionary of country and it's dial code pair.
##dial_codes=[(86,'China'),
##            (91,'India'),
##            (1,'US'),
##            (62,'Indonesia'),
##            (55,'Brazil'),
##            (92,'Pakistan'),
##            (880,'Bangladesh'),
##            (234,'Nigeria'),
##            (7,'Russia'),
##            (81,'Japan')]
##print({country:code for code,country in dial_codes})

##8.Building a dict whose price value is more than 200.
##prices={'ACME':45.23,'APPL':612.78,'IBM':205.55,'HPQ':37.20,'FB':10.75}
##
##print({company:price for company,price in prices.items() if price>200})
##


    


