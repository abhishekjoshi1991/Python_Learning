#For Loops

'''
for loop requires iterator to iterate through, like list, a tuple,
a dictionary, a set, or a string'''

#Loop control statements--> Loop control statements changes
#execution of loop from its normal sequence.


#1. Continue-->It returns the control to the beginning of the loop

for i in 'abhishek':
    if i=='i':
        continue
    print('current letter:',i)

#------------------------------------------------------------------------

#2. break -->It brings control out of the loop
    
print('\n')
for i in 'abhishek':
    if i=='s':
        break
    print('current letter:',i)


print('\n')
s = 'geeksforgeeks'
# Using for loop  
for letter in s:  
    
    print(letter)  
    # break the loop as soon it sees 'e'  
    # or 's'  
    if letter == 'e' or letter == 's':  
        break
    
print("Out of for loop")

'''
in above example, last print statement 'out of for loop' is executed
even if loop is break,this does not happen in for-else loop as explained below''' 
#------------------------------------------------------------------------

#3.pass
'''
for loops cannot be empty, but if you for some reason have a for loop
with no content, put in the pass statement to avoid getting an error.
'''

#------------------------------------------------------------------------

#else in for loop:
'''The else keyword in a for loop specifies a block
of code to be executed when the loop is finished successfully, it doesnot
execute else part if loop is stopped by break statment or error occured'''


for i in range(3):
    print(i)
else:
    print('finish!!')


#and see following program

print('\n')
for i in range(3):
    if i==2:
        break
    print(i)
else:
    print('finish!!')
