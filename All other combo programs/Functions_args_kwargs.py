#Variable Number of Arguments (*args and **kwargs)
 
'''
to pass variable or any number of arguments while calling the
function, these methods are used

Now see,
if we want to find out sum of two numbers using function,

def func(a,b):
    return sum(a,b)

if we call the function with some arguments then it will throw an
error that int object is not iterable, so this sum function requires
a tuple to carry the sum.

so program must be
def func(a,b):
    return sum((a,b))
'''
#++++++++++++++++++++++++++++++++++++++++++++++++++
#*args: arbitary arguments or non keyword arguments
#++++++++++++++++++++++++++++++++++++++++++++++++++
'''
when we have to pass multiple number of arguments inside a function,
then we use arbitary arguments or *args

it is impractical to use 10 variables for doing sum of 10 numbers
like
def func(a,b,c,d,e,f,g,h,i,j):

so instead of this we can use
def func(*a):


what *args does exactly?
it gathers all value those are passed while calling the function and
put it in a tuple for next computation. so in this way we receive
tuple of arguments using *args method

we can use any variable name after *, but good to use *args only
'''

#program to make sum of any number of numbers:
print('\n')
print('use of *args')
def func1(*args):
    return sum(args)

print(func1(10,30,40,50,60))#can pass any number of arguments


#Program to print square of arbitary numbers in a list
print('\n')
def f1(*nums):
    res=[]
    for i in nums:
        res.append(i**2)
    return res
print(f1(1,2,3,4))



print('\n')
def fun(*args):
    return 'My name is '+args[2]

print(fun('a','b','abhi','s'))


#++++++++++++++++++++++++++++++++++++++++++++++++++
#**kwargs: keyword arguments
#++++++++++++++++++++++++++++++++++++++++++++++++++

'''
to pass the arguments with key-value pair

this way function receives dictionary of arguments
'''

def keywarg(**kwargs):
    return 'youngest child is '+kwargs['B']

print(keywarg(A='emily',B='Watt',C='Mike'))

'''
don't use 'A'='emily','B='Watt'------
'''

#++++++++++++++++++++++++++++++++++++++++++++++++++
#combination of *args and **kwargs
#++++++++++++++++++++++++++++++++++++++++++++++++++


def comb(*args,**kwargs):
    return 'i want {} {}'.format(args[1],kwargs['food'])

print(comb(2,4,5,6,8,food='carrot',juice='orange'))
