If statement
1.WPTC User entered number is even
num=int(input("Enter a number: "))
if num%2==0:
    print("Entered number is even")


2.WPTC User entered number is positive
num=int(input("Enter a number: "))
if num>0:
    print(f"Entered Number is positive {num}")


3.WPTC User entered number is divisible by 5 and 3
num=int(input("Enter a number: "))
if num%5==0 and num%3==0:
    print(f"{num} is divisble by 5 and 3 ")


4.WAPT Check whether the string is startwith vowel
string=str(input("Enter the string: "))
if string.startswith(('a','e','i','o','u','A','E','I','O','U')):
if  string[0]=='a'or string[0]=='e' or string[0]=='i' or string[0]=='o' or string[0]=='u':
if  string[0] in ('a','e','i','o','u','A','E','I','O','U'):
if  string[0] in 'AEIOUaeiou':
    print(f"{string} startswith vowel")


5.WAPT check whether the given char character is uppercase
char=input("Enter the Char: ")
if char.isupper():
if char[0] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
if char>='A' and char<='Z':
if 'A'<=char<='Z':
    print(f"{char} is upper")


6.WAPT to check whether given data is list or not 
data=eval(input("Enter the List Data: "))
if type(data)==list:
    print("Entered data is correct")


If-else:
1.WAPT to check whether given data is list or not 
data=eval(input("Enter the List Data: "))
if type(data)==list:
    print("Entered data is correct")
else:
    print("Entered data is incorrect")


2.WPTC whether given character is lowercase or not
data=input("Enter the Data: ")
if data.islower():
    print("Entered data is lower")
else:
    print("Entered data is not lower")


3.WAPT check to given character special symbol
data=input("Enter the Data: ") 
if not data.isalnum():
    print("Entered data has special symbol ")
else:
    print("Entered data has not special symbol")


4.WAPT check whether the given data is single value datatype or not.
data=eval(input("Enter the Data: "))
if type(data)==int or float or complex or bool:
if type(data) in [int, float, complex, bool]:
    print(f"Entered Data is Single Value DataType ie {type(data)}")
else:
    print(f"Entered Data is not Single Value DataType ie {type(data)}")


5. WAPT check whether the given string is having more than 5 characters or not.
data=input("Enter the Data: ")
if len(data) > 5:
    print(f"Entered Data has more than 5 characters ie {len(data)}")
else:
    print(f"Entered Data has not more than 5 characters ie {len(data)}")


elif statement
1.WAPT to check relation between two integer numbers.
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
if num1>num2:
    print("First number is greater than Second number")
elif num2>num1:
    print("Second number is greater than first number")
else:
    print("First number is equal to Second Number")


2.WAPT check whether given character is uppercase or lowercase or digit or special symbol.
data=input("Enter the Char: ")
if data.isupper(): #'A'<=data<='Z':
    print("Entered data is Uppercase")
elif data.islower():#'a'<=data<='z':
    print("Entered data is Lowercase")
elif data.isdigit():#'0'<=data<='9'
    print("Entered data is digit")
else:
    print("Entered data is special symbol")


3.WAPT check whether given integer number is a single digit no. or double digit no. or 3 digit no. or more than 3 digit.
num=int(input("Enter a number: "))
if -9<=num<=9:
    print("Number is single digit number")
elif -99<=num<=99:
    print("Number is double digit number")
elif -999<=num<=999:
    print("Number is triple digit number")
##elif -1000 > num > 1000:#DOBUT
else:
    print("Number is more than 3 digit number")
##else:
##    print("invalid number")


4.WAPT to find the greatest among 4 numbers.
num1=int(input("Enter first number to compare :"))
num2=int(input("Enter second number to compare :"))
num3=int(input("Enter third number to compare :"))
num4=int(input("Enter fourth number to compare :"))
if num1>num2 and num1>num3 and num1>num4:
         print(f"First number is Greatest among 4 numbers ie {num1} is greater than {num2 ,num3 ,num4}")
elif num2>num1 and num2>num3 and num2>num4:
         print(f"Second number is Greatest among 4 numbers ie {num2} is greater than {num1 ,num3 ,num4}")
elif num3>num1 and num3>num2 and num3>num4:
         print(f"Third number is Greatest among 4 numbers ie {num3} is greater than {num1 ,num2 ,num4}")
else:
    print(f"Fourth number is Greatest among 4 numbers ie {num4} is greater than {num1 ,num2 ,num3}")


5.Print different words depending on whether a number is divisible by 3,5 or both .
if divisible by 3 -> "Fizz"
if divisible by 5 -> "Buzz"
if divisible by both -> "FizzBuzz"
num=int(input("Enter the Number :"))
if num%3==0:
    print("Fizz")
elif num%5==0:
    print("Buzz")
elif num%3==0 and num%5==0:
    print("FizzBuzz")
else:
    print("Python is Ez")


6.WAP that accepts the percentage of a student and prints the result classification based on the following criteria:
Percentage >= 75 -> Distinction
Percentage >= 60 and < 75 -> First Class
Percentage >= 50 and < 60 -> Second Class
Percentage >= 40 and < 50 -> Pass
Percentage < 40 -> Fail
percentage=int(input("Enter Your Percentage (0-100): "))
if 100 >= percentage >= 75:
    print("Distinction")
elif  60 <= percentage < 75 :
    print("First Class")
elif  50 <= percentage < 60 :
    print("Second Class")
elif 40 <= percentage < 50 :
    print("Pass")
elif percentage < 40:
    print("Fail")
else:
    print("Invalid Input") 


Nested if statement
1.WAP to check whether the given data is string or not , if it is check whether the length of string is multiple of 5 or not.
data =eval(input("Enter the data :"))
if type(data)==str:
    print("Entered data is string datatype")
    if len(data)%5==0:
        print("Length of entered data is multiple of 5")
    else:
        print("Length of entered data is not multiple of 5")
else:
    print("Entered data is not string datatype")


2.WAP for Instagram Login.
user_name="om@1234"
pass_word="omsawant"
username=input("Enter the username :")
if username==user_name:
    password=input("Enter the password :")
    if password==pass_word:
        print("Congratulations, You have successfully logged-in")
    else:
        print("You have entered wrong password")
else:
    print("You have entered wrong username")

username=input("Enter the username :")
password=input("Enter the password :")
if user_name==username:
    if password==pass_word:
        print("Congratulations, You have successfully logged-in")
    else:
        print("You have entered wrong password")
else:
    print("You have entered wrong username")


3.WAP to check whether the entered data is collection datatype or not , if it is then check whether it is mutuable datatype or not.
data=eval(input("Enter the data :"))
if type(data) in [str,list,tuple,dict,set]:
    print("Entered data is collection datatype")
    if type(data) in [list,dict,set]:
        print(f"Entered data is mutuable datatype ie {type(data)}")
    else:
        print(f"Entered data is immutuable datatype ie {type(data)}")
else:
    print("Entered data is not collection datatype")


4.WAP to check whether the given data is list or not , if it is a list then check that list having the middle value or not.
data=eval(input("Enter the list data :"))
if type(data)==list:
    print("Entered data is list datatype")
    if len(data)%2!=0:
        print("Entered data has middle value")
    else:
        print("Entered data has no middle value")
else:
    print("Entered data is not list datatype")


5.WAP to find the greatest among 3 numbers by using nested if statement without using and operator and elif keyword.
num1=int(input("Enter first number to compare :"))
num2=int(input("Enter second number to compare :"))
num3=int(input("Enter third number to compare :"))
if num1>num2:
    if num1>num3:
        print("Num1 is greatest among 3 numbers")
    else:
        print("Num3 is greatest among 3 numbers")
if num2>num3:
    print("Num2 is greatest among 3 numbers")
        
6. WAPT GIVEN CHARACTER IS ALPHABET OR NOT IF IT IS ALPHABET THEN
CHECK WHETHER IT IS VOVELS OR CONSONENT
char = input("Enter a character: ")

if char.isupper() or char.islower():
    print('Yes it is alphabet')
    if char in 'aeiouAEIOU':
        print("It is Vowel")
    else:
        print("It is Consonent")
else:
    print("Not an Alphabet")


WAP given list 5 times
data=input("Enter the list :")
print(data*5)

