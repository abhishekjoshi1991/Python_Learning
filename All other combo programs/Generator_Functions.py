#Generators Function

'''
A generator-function is defined like a normal function,
but whenever it needs to generate a value, it does so with the yield
keyword rather than return. If the body of a def contains yield,
the function automatically becomes a generator function.


return word gives value to user directly but
yield stroes that value to memory, thus yield gives generator object at o/p.

to get the values, either we can iterate over it or type cast that into list
or tuple
'''

#fibonaaci series with print statement
def fib(n):
    a,b=0,1
    while a<=n:
        print(a)#print statement will print all values
        a,b=b,a+b

fib(8)

#fibonaaci series with return statement
print('\n')
def fib(n):
    a,b=0,1
    while a<=n:
        return a#return will not print all values of sequence
        a,b=b,a+b

fib(8)

#fibonaaci series with yield statement
print('\n')
def fib(n):
    a,b=0,1
    while a<=n:
        yield a#return will not print all values of sequence
        a,b=b,a+b

for i in fib(8):#so only after iterating over fib we get values
    print(i)


'''
we can call individual values through generator function using __next__method
'''
print('\n')
def fib(n):
    a,b=0,1
    while a<=n:
        yield a
        a,b=b,a+b
x=fib(8)
print(x.__next__())#generates one value at a time
print(x.__next__())


#program to generate squares of a number for 1 to 10 numbers
print('\n')
def sq():
    i=1
    while True:
        yield i**2
        i+=1

for i in sq():
    if i>100:
        break
    print(i)
