#Python namespaces (Global, Local Variables) and Variable Scope:
#***************************************************************
'''
Namespaces is basically a system which keep track of all variables used inside
a program, can be checked using dir() function

we can reuse same names in python, like x can be used mutilple times. by using module.function()
we can reuse the name (Amulya's academy video). thus though function name is same but module name
is different then we can reuse the names.
'''

#let's take one example first of variable scope
print('variable scope')
print('*'*50)
print('program 1')
def func():
    x = 5
    return 'from inside of function:',x
print(func())
#print(x)

'''
in above program, we have defined the variable x inside the function
this variable scope is limited to that function only
thus we can say x is local variable for function

this x variable is not available globally to use
hence print(x) statement will give an error when it is written outside the
function

this is concept of variable scope
'''
#===========================================================================

#now take a look at below program

print('\n')
print('*'*50)
print('program 2')
x = 10
def func():
    x = 5
    return ('from inside of function:',x)
print(func())
print('from outside of fucntion:',x)

'''
in above example, we have defined x=10 as Global variable, it is available everywhere
for use, inside the function also (if no local variable is assigned with same name)

in above e.g. Local variable with same name x, is defined, thus after calling the function 
it will print value of 5 and not 10

if we don not specify Local value of x inside the function then see the o/p from below program
'''
#=============================================================================================
print('\n')
print('*'*50)
print('program 3')
x = 10
def func():
    return ('from inside of function:',x)
print(func())
print('from outside of fucntion:',x)

'''
in above program, value of x =10 is available globally to use everywhere (inside function
also) thus after function called it has printed value of 10'''


#========================================================================================
'''
now if we want to change the value of global x inside the function then we do this
using global keyword as below
'''
print('\n')
print('*'*50)
print('program 4')
x = 10
def func():
    global x
    x = 20
    return ('from inside of function:',x)
print(func())
print('from outside of fucntion:',x)

#here we have changed the value of x globally to 20


#======================================================================================================
#Tips/ recap*

# 1. a variable defined inside a function is local to it. when function ends, that variable is destroyed
# 2. variables defined outside the function are called as global variable
# 3. inside the function the global keyword can be used to change value of variable to global scope
# 4. Try to avoid use of global keyword inside the function

#=======================================================================================================
'''
now what if we want to change value of x inside the function?
'''
print('\n')
print('*'*50)
print('program 5')
x=8
def fun2():
    #x=x*2 uncomment to see the error
    print(x)

fun2()

'''
in above program, x = 8 is global variable and when we try to change value of x
inside the function then x is treated as local variable which is not defined 
inside fun2()
that means we are changing global variable inside local scope which is not allowed,
we can change the value using global keyword

so we will get error as local variable x is referenced before assignment
'''

#====================================================================================

#above program can be run successfully by assigning global x inside the function
print('\n')
print('*'*50)
print('program 6')
x=8
def fun2():
    global x
    x=x*2
    print(x)

fun2()

#====================================================================================

# we can cross check the scope of variable using dir() function

print('\n')
print('*'*50)
print('program 7')
print('initially :', dir())
num = 20
def f1():
    n = 10
    print('inside the function:',dir())
f1()
print('outside the function:', dir())

#here variable n is available only with function


#***********************************************************************************
# LEGB Rule:
#***********************************************************************************

'''
1 . LOCAL: contains Names defined inside the current function (available to use only inside 
the function, locally available)
2. GLOBAL : contains names those are defined at the start of script or module (top level, available
to use through out the program)
3. enclosed scope: names defined inside any enclosed function or nested function
4. built in scope: contains names built in to python language from any module

'''
print('\n')
print('LEGB Rule')

y = 10 # global scope
def outer():
    z = 4   # enclosing scope / non local variable
    def inner():
        x = 4  # local scope
        print('x:', x)
        print('y inside the function inner:', y)
        print('z inside the function inner:', z)
    inner()
    print('z:', z)
outer()


'''
here above, variable z is not local as well as not global variable to inner function.
we can't access z outside the outer function. also we can not modify the non-local variable 
inside local scope

now we can use 'nonlocal' keyword to change the non local variable (enclosed variable) to
local scope as below 
'''
print('\n')
print('changing the non local variable inside local scope')

y = 10 # global scope
def outer():
    z = 4   # enclosing scope / non local variable
    def inner():
        x = 4  # local scope
        nonlocal z
        z = z+1
        print('x:', x)
        print('y inside the function inner:', y)
        print('z inside the function inner:', z)
    inner()
    print('z:', z) # it value get changed permanently
outer()


'''
print, len, range etc. are called as built in variable. those are already defined
in python.

SO python always searches variable in Local Scope, if not found then it searches
in enclosed scope, if also not found then it searches in global scope, if also not
found then it searches in built in scope, if also not found then it throws NameError
this called as LEGB rule


x = 5  #global
def f():
    x = 10  #enclosed
    def f1():
        x = 15 #local
        print(x)
    f1()
f()
'''