#input taken in form n=1 2 3 4 5
print('type1')
n=input('enter the numbers:')#enter values space seperated(1 2 3)
list1=[]
for i in n.split(' '):#if values seperated by , then use .split(',')
    list1.append(int(i))
print(list1)

summation=0
for each in list1:
    summation+=each

print(summation)


#also can be written as
print('type2')
b=[int(i) for i in input('enter:').split()]
print(sum(b))


#using list comprehensions
print('type3')
n=input('enter the numbers:')
list1=[int(i) for i in n.split()]
print(list1)
print(sum(list1))
