#Decorators in python:
#*********************

'''
Decorators are used to add functionality to an existing code.

Important*
we must know that everything in python are objects, Names (variables) that we
define are just identifiers for these objects.
Similaraly,
Functions are no exceptions, they are objects too (with attributes).
Various different names can be bound to the same function object.

this is similar to len() function, in which we can assign value
of len() to any other variable

before going for decorators, we must know following concepts
'''
#*******************************************************************************
#1. Function is also object in python
print('Function behaves as an object')
print('*'*30)
def first():
    return 'Hello'
print(first()) #calling first function
second = first #assigning one variable to first (i.e function) reference/object
#because variable are always assigned for objects
print(second())
#here we can see that, we can assign function to variable

#*******************************************************************************
#2. Function can be passed as an argument to different function
#just like map, filter, reduce in which we were passing lambda func as an args
print('\n')
print('Function can be passed as an argument to other function')
print('*'*50)
def inc(x):
    return x+1
def dec(x):
    return x-1
def operate(func,num):
    return func(num)

print(operate(inc,5)) #here we passed inc as an argument to operate function
print(operate(dec,5))

#*******************************************************************************
#3. Function can return another function
'''
Here, is_returned() is a nested function which is defined(become operational) and
returns its value each time when we called is_called function, because for is_called
function we are return o/p from nested function
'''
print('\n')
print('Function can return another function')
print('*'*50)
def is_called():
    def is_returned():
        return 'I am from is_return function'
    return is_returned

#here if we say return is_returned() then after calling is_called directly
#we will get o/p as I am from is_return function but we call only
#return is_returned then after calling is_called, is_returned fucntion's
#object will be returned

print(is_called()) #we can call like this
#we need to store is_called() to some variable, and
#then that variable must be called again
new = is_called()
print(new()) #new() will start behaving as is_returned function
