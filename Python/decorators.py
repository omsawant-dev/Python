##1.Wap to create and use two decorators at same time.
##from time import sleep
##def delay(func):
##    def wrapper(n,*args,**kwargs):
##        sleep(n)
##        return func(*args,**kwargs)
##    return wrapper
##
##def log(func):
##    def wrapper(*args,**kwargs):
##        print("Good Morning")
##        return func(*args,**kwargs)
##    return wrapper
##@delay
##@log
##def greet():
##    return "Hello world"
##@log
##@delay
##def greeting(name):
##    return f"Hello {name}"
##@log
##def add(a,b):
##    return a+b

##2.create a decorator,it should reverse the other functions result if it is a string , otherwise
##it should return as it is
##def reverse(func_add):
##    def wrapper(*args,**kwargs):
        
##customize decorators
##from time import sleep
##def _delay(n):
##    def delay(func):
##        def wrapper(*args,**kwargs):
##            sleep(n)
##            return func(*args,**kwargs)
##        return wrapper
##    return delay
##
##def log(func):
##    def wrapper(*args,**kwargs):
##        print("Good Evening")
##        return func(*args,**kwargs)
##    return wrapper
##
##@_delay(4)
##def greet():
##    return "Hello world"
##
##@_delay(5)
##def greeting(name):
##    return f"Hello {name}"
##
##@_delay(3)
##def add(a,b):
##    return a+b
##
##@_delay(2)
##def mul(a,b,c):
##    return a*b*c


##3.customize log message
def _log(msg):
    def log(func):
        def wrapper(*args,**kwargs):
            print(f"Good {msg}")
            return func(*args,**kwargs)
        return wrapper
    return log

@_log('Morning')
def add(a,b):
    return a+b

@_log('Evening')
def mul(a,b,c):
    return a*b*c

@_log('Afternoon')
def greet():
    return "Hello world"











