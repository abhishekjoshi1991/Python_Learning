#Factorial Program

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#Method-1
print('using for loop')
factorial=1
num=int(input('enter number for which factorial wants:'))
for i in range(2,num+1):#not neccessary to start rane from 1
    factorial=factorial*i


print(factorial)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#Method-2
print('\n')
print('using while loop')
num=int(input('enter number for which factorial wants:'))
factorial=1
i=2
while i<=num:
    factorial=factorial*i
    i+=1
print(factorial)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#Method-3, with reduced no of steps
print('\n')

num=int(input('enter number for which factorial wants:'))
fact=1
while num>1:
    fact=fact*num
    num=num-1
print(fact)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#Method-4, using user defined functions
print('\n')
print('using functions')
def fact(num):
    fact=1
    for i in range(2,num+1):
        fact=fact*i
    return fact
print(fact(5))

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#Method-5, using recursion
print('\n')
print('using recursion')
def facto(num):
    if num<=1:
        return 1
    else:
        return num*facto(num-1)
print(facto(5))

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
