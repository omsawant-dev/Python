##1.Armstrong
##num=int(input("enter the number :"))
##l=len(str(num))
##temp=num
##Sum=0
##i=0
##while i<l:
##    digit=temp%10
##    Sum=Sum+digit**l
##    temp=temp//10
##    i+=1
##
##if Sum==num:
##    print("Armstrong")
##else:
##    print("Not Armstrong")
    
##2.Prime or not
##num=int(input("enter the number :"))
##i=1
##count=0
##while i<num+1:
##    if num%i==0:
##        count+=1
##    i+=1
##if count<=2:
##    print("Prime number")
##else:
##    print("Not a prime")
        
##3.GCD
##num1=int(input("enter the number 1 :"))
##num2=int(input("enter the number 2 :"))
##gdc=0
##for i in range(1,min(num1,num2)):
##    if num1%i==0 and num2%i==0:
##        gdc=i
##
##print(gdc)

##4.LCM of two numbers
##a = int(input("Enter first number: "))
##b = int(input("Enter second number: "))
##
##lcm = max(a, b)
##
##while True:
##    if lcm % a == 0 and lcm % b == 0:
##        print("LCM:", lcm)
##        break
##    lcm += 1

##5. reverse a number without using slicing.

##def is_prime(num):
##    if num <= 1:
##        return False
##    for i in range(2, int(num**0.5) + 1):
##        if num % i == 0:
##            return False
##    return True
##
##num = int(input("Enter the number :"))
##print("Prime" if is_prime(num) else "Not Prime")



##num = int(input("Enter the number :"))
##temp = num
##n = len(str(num))
##sum_val = 0
##
##while temp > 0:
##    digit = temp % 10
##    sum_val += digit ** n
##    temp //= 10
##
##print("Armstrong" if sum_val == num else "Not Armstrong")
##

##num = int(input("Enter the number :"))
##temp=num
##Sum=0
##n=len(str(num))
##
##while temp > 0:
##    digit=temp%10
##    Sum=Sum+digit**n
##    temp//=10
##
##
##print("Armstrong" if Sum==num else "Not Armstrong")


##num = int(input("Enter the number :"))
##original = num
##rev = 0
##
##while num > 0:
##    rev = rev * 10 + num % 10
##    num //= 10
##
##print("Palindrome" if original == rev else "Not Palindrome")


##n = int(input("Enter the number :"))
##
##a, b = 0, 1
##for _ in range(n):
##    print(a, end=" ")
##    a, b = b, a + b
##
##a,b=0,1
##for i in range(n):
##    print(a,end=" ")
##    a,b=b,a+b
##

##n=int(input("Enter the number :"))
##fact=1
##for i in range(1,n+1):
##    fact*=i
##print(fact)

##lst=[10, 20, 99, 99, 45]
##first=second=0
##for num in lst:
##    if num > first :
##        second = first
##        first = num
##    elif num > second and num != first:
##        second = num
##
##print(second)

##s1 = input()
####s2 = input()
##
####print("Anagram" if sorted(s1) == sorted(s2) else "Not Anagram")
##print("Palindrome" if s1==s1[::-1] else "Not a Palindrome")

##lst=eval(input("enter the list :"))
####result=[]
####for i in lst:
####    if i not in result:
####        result.append(i)
####print(result)
##Sum=0
##for i in lst:
##    if type(i)==int:
##        Sum+=i
##print(Sum)


lst=eval(input("enter the list :"))
##total = 0
##
##for num in lst:
##    while num > 0:
##        total += num % 10
##        num //= 10
##
##print(total)        

max_val = min_val = lst[0]

for num in lst:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num

print("Max:", max_val)
print("Min:", min_val)



















    
              
