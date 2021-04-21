#Closures

'''
a closure is function object that remembers the values in enclosing scopes even if
they are not present in memory
'''

# Before going to closure let's take look on concepts below,
# (refer amulya's academy video: https://www.youtube.com/watch?v=tvWRhMkUcoU&list=PLzgPDYo_3xukWUakgF-OJvDOChq6drPG2&index=4)


'''
we know that functions are an object in python from Decorators_Introduction.py file
i.e. we can store reference of some def f():   into other variable g=f, then we can call g()

Now w know that,  we can use enclosed variable inside the nested function (locally).
'''
print('\n')
print('using enclosed variable inside local function')
print('*'*50)
def outer():
    x = 5   #enclosed variable
    def inner():
        print(x)  #non value returning function as we have used print statement
    inner()  #function call
outer()  # we can call outer function without using print statement

'''
so as seen in above example, x = 5 is in enclosed scope, we can use that inside local function named
as inner. also we have called inner() function inside outer function. 

But we can not call inner function outside, means we can not write code as 

def outer():
    x = 5   #enclosed variable
    def inner():
        print(x)  #non value returning function as we have used print statement
    inner()
inner()  
outer()

we will get name error as inner is not defined.


Now instead of calling inner function inside the outer function, we will return the inner function.
as we are returning the inner function in outer function, we can use variable 'a' to store outer call, 
means

'''
print('\n')
print('returning inner function inside the outer function, and store result to variable')
print('*'*90)
def outer():
    x = 5   #enclosed variable
    def inner():
        print(x)  #non value returning function as we have used print statement
    return inner() #function call

a  = outer()
print(a)

'''
here we will get o/p as 5 and none, None because inner is non value returning function.
if we have used return statement for inner function then we will not get None


Now again, instead of calling inner function in return of outer function, we can use 
return inner then it means that we returning reference of inner function to outer function.

see as below
'''

print('\n')
print('returning reference of inner function to outer function')
print('*'*90)
def outer():
    x = 5   #enclosed variable
    def inner():
        print(x)  #non value returning function as we have used print statement
    return inner # Not calling the function

a  = outer()
print(a)
print(a.__name__)


'''
so in above we are clear that on outer function call we are returning reference of 
inner function. so a.__name__ gives answr as inner and not outer. that means 'a' is
nothing but inner function


Now take example as below
'''

print('\n')
print('calling the inner function outside its scope')
print('*'*90)
def outer():
    x = 5   #enclosed variable
    def inner():
        y = 50
        return x+y #now it is value returning function
    return inner # Not calling the function

a  = outer()
print(a())

'''
now we know that 'a' refers to inner function and we also know that we can not
call inner function outside, then how it is possible that after calling a() o/p
is 55. as 'a' refers to inner and we are calling it outside also, this concept is called as
closure where we can excute the inner/nested fucntion outside its scope..

so even if we have finished with execution of outer function at line 106, value of x from
enclosing scope is remembered, this is closure concept. 

So to have a closure we must have,
1. we need nested function
2. nested function must refer some value that are defined in enclosing scope i.e. here x = 5
3. enclosing function (outer) must return nested function (inner)


Uses:
1. data hiding
2. we can avoid use of global value
'''

print('\n')
print('example from ethans class')
print('*'*90)
def multiplier_of(n): #here we are not passing function as argument
    def multiplier(number):
        return n*number
    return multiplier


multiplywith5 = multiplier_of(5) #5 will go as arg into outside function
#when control will go to the inner multiplier function then it remembers
#that 5 value from enclosed function (i.e multiplier_of()) to be put in 5*number,
# so when we called multiplywith5 with
#some number then result is printed

print(multiplywith5(9))


'''
so if we pass function as an argument to multiplier_of() function then it becomes decorator
and when we pass other that function as an argument (here n) then it becomes closure


it remembers value of enclosing scope even if that value does not exists in memory, so even if we delete
the function value is printed, see below e.g from video link
' https://www.youtube.com/watch?v=3XRSULw-HlE'
'''
print('\n')
print('last example')
def outer(text):
    def inner():
        print(text)
    return inner
a = outer('hello')
del outer
a()  #even after deleting the function, value is remembered
