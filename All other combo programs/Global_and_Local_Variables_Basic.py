#Global and Local Variables in Python
#Important

'''Global variables are those which are defined outside the function
and they are used inside the function'''

#=============================================================================
'''type 1-global variable defined outside and called inside the function'''

def func():
    print(a)

#global scope
a=10    #a can be defined before function also
func()

#=============================================================================
print('\n')
'''type 2-local variable a is assigned inside function before print statement'''

def func():
    a=25
    print(a)

#global scope
a=100
func()
print(a)

#==============================================================================
print('\n')
'''type 3- local variable is called before assignment i.e. print statement is
before assigning local variable'''

def func():
    #print(a)   #this line gives error, uncomment to error
    a=25
    print(a)

#global scope
a=100
func()
print(a)

#=============================================================================

print('\n')
'''to remove this error global keyword has to be used before calling'''

def func():
    global a
    print(a)  #error eliminated as a will consider global a i.e 100
    a=25      #this value now considered as globally
    print(a)  #here a is local a i.e 25

#global scope
a=100
func()
print(a)   #it will updated global value not 100 value because function is called
#before this statment and value of a has changed globally to 25

#=============================================================================

#example


a = 1

# Uses global because there is no local 'a' 
def f(): 
	print('Inside f() : ', a) 

# Variable 'a' is redefined as a local 
def g():	 
	a = 2
	print('Inside g() : ', a) 

# Uses global keyword to modify global 'a' 
def h():	 
	global a 
	a = 3
	print('Inside h() : ', a) 

# Global scope 
print('global : ',a) 
f() 
print('global : ',a) 
g() 
print('global : ',a) 
h() 
print('global : ',a) 


