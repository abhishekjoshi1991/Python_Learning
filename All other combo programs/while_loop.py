#all about while loop

'''
syntax:

while expression:
    statement(s)
'''

n=1
while n<=5:
    print('square of ',n,'is',n**2)
    n+=1
print('successful')

#----------------------------------------------------------------------
#while-else loop

'''
As discussed above, while loop executes the block until a condition
is satisfied. When the condition becomes false, or loop is breaked
the statement immediately after the loop is executed.(SEE P1)

The else clause is only executed when your while condition becomes false.
If you break out of the loop, or if an exception is raised,
it won’t be executed.(SEE P2)
'''
#P1
print('\n')
n=1
while n<=5:
    print('square of ',n,'is',n**2)
    n+=1
    if n==3:
        break
print('successful')

#P2
n=1
print('\n')
while n<=5:
    print('square of ',n,'is',n**2)
    n+=1
    if n==3:
        break
    
else:
    print('successful')


#in P1, even if loop is break, statement after while loop is executed
#but in P2,loop is breaked hence it wont execute else part, if break statement
#is commented then else part will get executed, means else part executed only
#when while loop is executed totally or while False is come

#-----------------------------------------------------------------------------


#continue keyword in while loop
    
'''when continue word is hit during execution of program then, python doesn't
look/go to any statement after continue word, rather it goes again to
the while loop

It brings the control to the beginning of the loop, without executing statments
after it.
'''

#square of numbers from 1 to 10, with continue statement in program

'''
#Prog 1, this will go in infinite loop
i=1
while i<=10:
    print('square of ',i,'is',i**2)
    if i==7:
        continue
    i+=1
else:
    print('finish')
'''

#------------------------------------------------------------------------------

#Program 2, print square of nums upto 10 except 7
print('\n')
print('o/p with increment--continue--print')
i=0
while i<=9:
    i+=1
    if i==7:
        continue
    print('square of ',i,'is',i**2)
else:
    print('finish')

#or
print('\n')
i=1
while i<=10:
    if i==7:
        i+=1
        continue
    print('square of ',i,'is',i**2)
    i+=1
else:
    print('finish')

#------------------------------------------------------------------------------
'''
#Program 3,this is also infinite loop, but it stucks in shell by giving o/p
print('\n')
print('o/p with continue--print--increment')
i=1
while i<=10:
    if i==7:
        continue
    print('square of ',i,'is',i**2)
    i+=1
else:
    print('finish')
'''
#==============================================================================

#break keyword in while loop
#It brings control out of the loop, mainly it breaks from inner enclosing loop
#see program ABC downwards

print('\n')

print('o/p with print--break--increment')
i=1
while i<=6:
    print(i)
    if i==4:
        break
    i+=1

print('\n')
print('o/p with break--print--increment')
i=1
while i<=6:
    if i==4:
        break
    print(i)
    i+=1

print('\n')
print('o/p with increment--break--print')
i=1
while i<=6:
    i+=1
    if i==4:
        break
    print(i)

''' this will go in infinite loop

print('\n')
i=1
while i<=6:
    if i==4:
        break
    print(i)
i+=1
'''
#==============================================================================

#break words breaks from inner enclosing loop means

#Program ABC
print('\n')
print('break from inner enclosing loop means')
i=1
while i<=10:
    while i<=7:
        if i==6:
            break
        print('square is:',i**2)
        i+=1
    else:
        print('cube is:',i**3)
    i+=1
#it does not stop iteration at i=6, rather it breaks from i<=7 while loop and
    #not i<=10 while loop
