##sorted (inbuild function)
names=('microsoft','apple','google','TCS','IBM','wipro','capgemini','Ey')
##print(sorted(names))
##print(sorted(names,key=lambda name:name[-1]))
##print(sorted(names,key=lambda name:name[-1],reverse=True))
##d={'anna':20000,'bob':10000,'malhar':5000,'om':40000,'kshtij':30000}
##print(sorted(d))
##print(sorted(d,key=lambda k:d[k]))

lst1=[4,2,4,10,40]
lst2=[5,3,6,7,8,1]
##
##merge and sort
##print(sorted(lst1+lst2))
##
##sort and merge
##print(sorted(lst1)+sorted(lst2))

##Reverse(iterator)
st='apple'
print(list(reversed(st)))
print(''.join(reversed(st)))
print(list(reversed(lst1)))
print(tuple(reversed(names)))
