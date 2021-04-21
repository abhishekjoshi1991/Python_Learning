#Program for fibonacci series(1,1,2,3,5,8,13,21...)


#Program 1

x=0
y=1
print(y)
i=1
while i<=10: #to print series upto 10 lines, can use for loop also
    a=x+y
    x=y
    y=a
    print(y)
    i+=1

#=======================================================================
#Program 2
print('\n')
print('o/p of second program')
x,y=0,1
print(y)
for i in range(10):
    x,y=y,x+y
    print(y)
    
    
#=======================================================================
#Program 3: using recursion
'''
in fibonacci series, All other terms are obtained by adding the preceding
two terms.This means to say the nth term is the sum of (n-1)th and (n-2)th
term.
'''
print('\n')
print('program using recursion:')
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)

nterms=int(input('enter upto long series is required:'))
for i in range(nterms):
    print(fib(i))
