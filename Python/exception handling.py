##Specific Error
##def div():
##    try:
##        a=int(input("Enter the value for a :"))
##        b=int(input("Enter the value for b :"))
##        c=a/b
##        print(c)
##    except ZeroDivisionError:
##        print("The value of b should not be zero")
##        div()
##
##div()

##generic error
##def div():
##    try:
##        a=int(input("Enter the value for a :"))
##        b=int(input("Enter the value for b :"))
##        c=a/b
##        print(c)
##    except Exception as e:
##        print(e)
##        div()
##
##div()

##default error
##def div():
##    try:
##        a=int(input("Enter the value for a :"))
##        b=int(input("Enter the value for b :"))
##        c=a/b
##        print(c)
##    except:
##        print("Exception is being handled")
##        div()
##
##div()


##User defined exception
##a=int(input("Enter a :"))
##b=int(input("Enter b :"))
##
##if a>b:
##    print(a+b)
##else:
##    raise ValueError ("a should be greater than b")

##assertion
a=int(input("Enter a : "))
b=int(input("Enter b :"))

assert a>b,("a should be greater than b")
print(a+b)
print('We can perform next operations using a and b')


























