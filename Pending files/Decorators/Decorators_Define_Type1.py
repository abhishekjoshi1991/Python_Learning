#Method 1- to define decorator, using decorator function within same file

#let's create decorate function definition first
def make_pretty(func):
    def inner():
        print('i am decorated')
        func()
    return inner

#let's create function which need to be decorated
def ordinary():
    print('i am ordinary')

#now apply make_pretty decoration to ordinary function
if __name__=='__main__':
    ordinary()
    print('*'*10)
    pretty = make_pretty(ordinary)
    pretty()
    print('*' * 10)

'''
In the example shown above, make_pretty() is a decorator. 
The function ordinary() got decorated and the returned function was given the name pretty.
We can see that the decorator function added some new functionality to the original function.

Generally, we decorate a function and reassign it as,

ordinary = make_pretty(ordinary)
'''

#*****************************************************************
'''
this won't work with return statement like below,

def make_pretty(func):
    def inner():
        return 'i am decorated'
        func()
    return inner


#let's create function which need to be decorated
def ordinary():
    return 'i am ordinary'

#now apply make_pretty decoration to ordinary function

if __name__=='__main__':
    ordinary()
    print('x'*10)
    pretty = make_pretty(ordinary)
    pretty()
    print('x' * 10)

when we use return statement in function, then we need to call the function
using print() function, as simple call will not return anything
and we know that once return is hit then block of code after it won't get
executed, so in definition of make_pretty we need to call func() first then
we can use return command

so above code we can write as,   
'''

print('\n')
print('o/p using return statements inside function definition')
def make_pretty(func):
    def inner():
        print(func())
        return 'i am decorated'
    return inner

def ordinary():
    return 'i am ordinary'

if __name__=='__main__':
    print(ordinary())
    print('x'*10)
    pretty = make_pretty(ordinary)
    print(pretty())
    print('x' * 10)

