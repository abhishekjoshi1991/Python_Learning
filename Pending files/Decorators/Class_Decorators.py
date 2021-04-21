# Watch video: 'https://www.youtube.com/watch?v=rXLhnlP5sMY&list=PLzgPDYo_3xukWUakgF-OJvDOChq6drPG2&index=7'
'''
before going to the class decorator, let's go through some programs
'''

# Program - 1
print('loosing data from function to be decorated')
print('*'*50)
def decorator(func):
    def inner():
        str1 = func()
        return str1.upper()
    return inner

@decorator
def greet():
    return 'good morning'

print(greet())
print(greet.__name__)

'''
in above example, when we print name of greet function, it gives reference of inner function
that means decorator hides some functionality/data of original function to be decorated

to regain its functionality we have to import functools from that we can use wraps decorator'''


# Program - 2
print('\n')
print('regaining the data from function to be decorated')
print('*'*50)
import functools
def decorator(func):
    @functools.wraps(func)
    def inner():
        str1 = func()
        return str1.upper()
    return inner

@decorator
def greet():
    return 'good morning'

print(greet())
print(greet.__name__)


'''
till now we have seen that how to apply decorator function on another function
let's now see how to apply decorator function on methods

we will create a class, in that we will validate based on name,
if name is abhishek then it will execute msg from decorator else
will execute print_name methode of class

here we will apply decorator on class method i.e. print_name
'''

# Program - 3
print('\n')
print('applying decorator on class methods')
print('*'*50)
def check_name(method): #parameter name method or func
    def inner(self_dec): #need to pass parameter as method to be decorated has parameter
        if self_dec.name == 'abhishek':
            print('hey my name is also same!!!')
        else:
            method(self_dec)
    return inner
class Printing:
    def __init__(self,name):
        self.name = name
    @check_name  #decorator applied here
    def print_name(self):
        print('entered user name is :', self.name)
p = Printing('abhi')
q = Printing('abhishek')
p.print_name()
q.print_name()



# We can also define class as a decorator instead of function

# Class Decorators:
#*********************

'''
before going to further let's understand the concept below:
when we call the class method of an instance of class then
__call__ method which is dunder method of may be
object class (top level above parent) is called

let's take example
'''
print('\n')
print('class decoraters')
class Printing:
    def __init__(self,name):
        self.name = name
    def print_name(self):
        print('entered user name is :', self.name)

p1 = Printing('sukanya')
p1.print_name()

'''
here after calling p1.print_name we get result because print_name
method is callable. but what happens when we call only p1 as p1()
it will show error that object is not callable, so we need to 
use __call__ method  then we can call
see below
'''

print('\n')
class Printing:
    def __init__(self,name):
        self.name = name
    def __call__(self):
        print('entered user name is :', self.name)

p1 = Printing('sukanya')
p1() #now we can call object also

# Let's create class decorator now, which will convert the string to uppercase
print('\n')
print('o/p of class decorator')
class Decorator():
    def __init__(self, func): #need to pass function to be decorated
        self.func = func
    def __call__(self):
        str1 = self.func()
        return str1.upper()

@Decorator
def greet():
    return 'good morning'
print(greet())

