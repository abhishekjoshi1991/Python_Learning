#Shallow copy vs deep copy
'''
In Python, we use = operator to create a copy of an object.
We may think that this creates a new object; it doesn't.
It only creates a new variable that shares the reference
of the original object (very imp line)

if we say
l1=[1,2]
l2=l1
l2.append(10)
print(l1)
print(l2)
here assignment operator =, changes both objects l1 and l2,
we dont want that during copying, so for mutable objects like
lsit, sets etc we  have to use shallow and deep copy

shallow copy:https://www.youtube.com/watch?v=zHMViQcLFjE
deep copy: https://www.youtube.com/watch?v=Riv6UJ6GFDM
'''

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 1. Shallow Copy

'''
shallow copy creates new object (e.g new list) which is derived
using memory reference number of original elements.

shallow copy can be created using 4 methods:
1. using built in functions of list, sets etc
2. using slicing operator
3. using list comprehensions
4. using copy function from copy module

'''
#1. using buit in function
l1=[1,2,3,4]
l2=list(l1)
print('new list:',l2)
l2.append(10)
print('original list:',l1)
print('new list after append:',l2)
print('\n')


#2. using slicing method
l1=[1,2,3,4]
l2=l1[:]
print('new list:',l2)
l2.append(10)
print('original list:',l1)
print('new list after append:',l2 )
print('\n')


#3. using list comprehensions
l1=[1,2,3,4]
l2=[x for x in l1]
print('new list:',l2)
l2.append(10)
l2[2]='a'
print('original list:',l1)
print('new list after append:',l2 )
print('\n')


#4. using copy module
import copy
l1=[1,2,3,4]
l2=copy.copy(l1)
print('new list:',l2)
l2.append(10)
l2[2]='abhi'
print('original list:',l1)
print('new list after append:',l2 )
print('\n')
'''
here in all above example, l1 does not change even if
we change the l2 by append method other other methods,
thus shallow copy creates new object(whole new list with other
memory location)

but
but
but

for nested objects (like nested list) it wont't work if we try to
change nested elements, then l1 will change as per the l2.
see below example
'''

#shallow copy on nested list-type 1
print('shallow copy on nested lists- type 1')
import copy
l1=[[1,2,3],4,5,6]
l2=copy.copy(l1)
print(l2)
l2.append(100)#here 100 is appended to non nested items
print(l1)
print(l2)
print('\n')

'''
here again only l2 is changed and not l1, as we have appended
items outside the nesting
'''


#shallow copy on nested list-type 2

print('shallow copy on nested lists- type 2')
import copy
l1=[[1,2,3],4,5,6]
l2=copy.copy(l1)
print(l2)
l2[0][1]='abhi'#here index value is changed within nested elements
l2[0].append(150)
print(l1)
print(l2)
print(id(l1)==id(l2))
print('\n')

'''
so here list l1 and l2 both gets changed, this is behaviour of shallow
copy on nested elements
though it altering both lists, but memory location
will be always different.
so to eliminate this drawback, deep copy is used
'''
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#2. Deep copy
'''
in deep copy, new object is created as shallow copy that means
memory location of l1 and l2 will be different.
but for nested elements , deep copy keeps original object
as it is , only changes happen in new object.
so basically deep copy is used for nested items.
its behaviour for non nested items will be same as shallow copy
'''

import copy
l1=[[1,2,3],4,5,6]
l2=copy.deepcopy(l1)
print(l2)
l2.append(150)#appending 150 to non nested items
print(l1)
print(l2)
print('\n')
'''here no effect as we adding elements to non nested items'''

import copy
l1=[[1,2,3],4,5,6]
l2=copy.deepcopy(l1)
print(l2)
l2[0].append(150)#appending 150 to nested items
print(l1)
print(l2)
print('\n')
'''here l1 will not change, only l2 will change'''








