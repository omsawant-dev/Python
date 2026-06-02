##Pattern Programming
##1.WAP to print :
##1
##1 2 
##1 2 3 
##1 2 3 4 
##1 2 3 4 5 
##num=5
##for i in range(1,num+1):
##    for j in range(1,i+1):
##        print(j,end=' ')
##    print()
##
##
##2.Wap to print given pattern
##for i in range(ord('A'),ord('E')+1):
##    for j in range(ord('A'),i+1):
##        print(chr(j),end=' ')
##    print()
##
###without ord function
##for i in range(65,70):
##    for j in range(65,i+1):
##        print(chr(i),end=' ')
##    print()
##
##for i in range(ord('A'),ord('E')+1):
##    for j in range(ord('A'),i+1):
##        print(chr(j),end=' ')
##    print()
##
##
##3.WAP to print given pattern
##num=5
##for i in range(num,0,-1):
##    for j in range(i):
##        print("*",end=' ')
##    print()
##
##for i in range(70,65,-1):
##    for j in range(i):
##        print(chr(i),end=' ')
##    print()
##
##
##
##num=5
##for i in range(1,num+1):
##    print('* '*i)
##
##num=5
##for i in range(num,0,-1):
##    print('* '*i)
##
##
##4.WAP to print given pattern
##num=5
##for i in range(num,0,-1):
##    for j in range(1,num+1):
##        if i<=j:
##            print("*",end=' ')
##        else:
##            print(" ",end=' ')
##    print()
##
##num=5
##for i in range(1,num+1):
##    print("  "*(num-i)+'* '*i)
##
####5.WAP
##num=5
##for i in range(num,0,-1):
##    for j in range(num,0,-1):
##        if i>=j:
##            print("*",end=' ')
##        else:
##            print(" ",end=' ')
##    print()
##
##num=5
##for i in range(num,0,-1):
##    print("  "*(num-i)+'* '*i)
##
##
####6.WAP
##num=5
##for i in range(1,num+1):
##    print(" "*(num-i)+'* '*i)
##
####7.WAP
##num=5
##for i in range(num,0,-1):
##    print(" "*(num-i)+ '* '*i)
##
##8.WAP
##num=5
##for i in range(1,num):
##    print(" "*(num-i)+'* '*i)
##for i in range(num,0,-1):
##    print(" "*(num-i)+ '* '*i)
##
##
##9.WAP
##num=5
##for i in range(1,num+1):
##    if i in (1,num):
##        print('* '*num)
##    elif i in (2,3,4):
##        print('* '*1)
##    else:
##        print(" "*(num-1))
##
##cols=5
##rows=5
##for row in range(1,rows+1):
##    if row in (1,rows):
##        print('* '*cols)
##    else:
##        print('*')
##
##10.WAP 
##cols=5
##rows=5
##for row in range(1,rows+1):
##    if row in (1,rows):
##        print('* '*cols)
##    else:
##        print('*'+'  '*(cols-2)+' *')
##
##
##
##
##
##
##
##
##
##
##
