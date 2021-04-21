#Functions or User Defined Functions

'''
function is set of statements those are executed when called

function takes data from user, process it and returns the result, it returns or
throws the value to user


def func(a,b):#a,b are formal parameters or positional arguments
    return a+b
print(func(10,20))#10,20 are actual parameters passed
'''

#function syntax

def func():
    '''
    docstring:(to store info about function)
    this is hello world fucntion
    '''
    return 'hello world'
print(func())
print(help(func))

#================================================================

#difference between print and return statement
'''
if we used print statement inside the function instead of return,
then by logic result does not get returning to user, it get printed
there only, (see function video for more explaination) means
'''

def func(a,b):
    print(a+b)

print(func(10,20))

'''
Now in above we have used print statement inside the function,
and also we are calling the function inside the print statement,

whenever we want result using print statement then it is always
expected to have return word inside the function, otherwise it
print the result also and print none value also,

below is correct
'''
print('\n')
def func(a,b):
    return a+b

print(func(10,20))

'''
so it is always better to use return word inside the function, it
also allows us to store the result in some variable, which won't
be possible using print statement
'''

def func(a,b):
    print(a+b)

sum=func(10,20)#no o/p 
print(sum)

print('\n')
def func(a,b):
    return a+b
sum=func(10,20)
print(sum)

#================================================================

#Rules:
'''
once return statement is hit, then python does not execute next
block of code irrespective of no. of iterations are pending
'''

print('\n')
def fun():
    return 'hello'
    return 'world'#only hello is printed
print(fun())

print('\n')
 
'''
python can return multiple value, but using single return statement
only
but it returns single object in that case

here below tuple of multiple values are printed'''

print('\n')
print('printing multiple value:')
def func(a,b):
    return a+b,a-b,a*b
print(func(20,10))


#================================================================

#default arguments
'''
default arguments takes default value which is passed while
defining the function, so while calling the function
if value is not passed for default argument then it takes default
value,

if value is passed then it throws the updated value while printing
'''
print('\n')
print('default arguments')
def stud(name,nation='india'):
    return name,nation

print(stud('abhishek'))#default value on nation is printed
print(stud('abhishek','US'))#new value of nation is printed
  
'''
main imp point:
default argument can't be passed for first positional argument
otherwise while calling the function, python will get confused
that which value to be taken for next positional arguments or
are we trying to change default argument, means

def func(a=10,b,c):
    return a+b+c
print(func(20,30))

#it will give the error that non default arguments are defined
#after default arguments that can't be possible

here python will get confused that 20 value is for a or for b

so always assign default arguments at last, means
def func(a,b=1,c=2):
    return a+b+c
print(func(20,30))

try to run this code in shell
'''
#================================================================
#================================================================




