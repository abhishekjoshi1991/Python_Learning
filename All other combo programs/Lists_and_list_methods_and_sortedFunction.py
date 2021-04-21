#Lists and its methods or object functions (generaaly strings and tuple does
#throw value after object function is called as they are immutable, but list
#does not throw any value generally, e.g l1.append() does not throw result)

'''Lists are just like dynamic sized arrays,single list may contain
DataTypes like Integers, Strings, as well as Objects. Lists are mutable,
and hence, they can be altered even after their creation.
List in Python are ordered and have a definite count.

A list may contain duplicate values with their distinct positions and hence,
multiple distinct or duplicate values can be passed as a sequence
at the time of list creation.
'''

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#List Methods-
# 1. Append
'''this method adds the element only at the end of list one at a time only.
to add multiple elements, loops are used.
tuples, list, strings can be added as a single element at the end of list
this method changes the parent list
append changes object hence does not throw anything
'''
print('append method')
l1=[1,2,3]
l1.append(4)
l1.append((10,20))
l1.append(['a','s'])
print(l1)
print('\n')

#===========================================================================

# 2. Extend
'''this method extends the list by appending elements from iterables.
here element must be in the form of iterable like list, tuple or string
but append only add single element
extend changes object hence does not throw anything
'''
print('extend method')
l1=[1,2,30]
#l1.extend(5,4,6), this won't work
l1.extend([10,20,30])
print(l1)
print('\n')


#===========================================================================

# 3. Insert
'''to add the element in the list at required index position, insert method is
used, this method takes two arguments, it inserts does not replace

syntax: l1.insert(index,value)

this method also changes the parent list
if index position is not given, then throws error
insert changes object hence does not throw anything
'''
print('insert method')
l1=[1,2,3]
l1.insert(1,'abhi')
print(l1)
print('\n')


#===========================================================================

#4.Copy
'''
Returns a copy of a list.
Shallow copy means the any modification in new list won’t be
reflected to original list.
copy does not changes object hence throws value
'''

l1=[10,20,30]
l2=l1.copy()
l2.append(40)
print(l1)#here no effect on l1 as append is carried out on l2
print(l2)
print('\n')

'''also if we change l1 by appending some value, then l2 wont print that appended
value
means
l1=[10,20,30]
l2=l1.copy()
l1.append(90)
print(l1) #o/p is [10,20,30,90]
print(l2) #o/p is [10,20,30]
'''

#===========================================================================

#5. pop
'''Remove and return (i.e print that value in shell)
item at mentioned index position, default index position
is last index.
Raises IndexError if list is empty or index is out of range
'''
print('pop method')
l1=[1,2,3,4,5,6]
l1.pop(0)
print(l1)
l1.pop()#without giving index position removes last item
print(l1)
print('\n')

#===========================================================================

#6. remove
'''
removes the first occurence from list
'''
print('remove method')
l1=[5,6,8,9,8,10,3,5]
l1.remove(8)
print(l1)
print('\n')

#===========================================================================

# del (its not actually a method, its a keyword)

'''
deletes all items within specified range'''
print('del')
l1=[5,6,8,9,8,10,3,5]
del l1[1:5]
print(l1)
print('\n')

#===========================================================================

# clear, this also not a method
'''removes all items from list'''

#===========================================================================

#7. index
'''
it searches for a given element from the start of the list and returns
the lowest index where the element appears

syntax: l1.index(valuetosearch, lower index(optional), upper index(optional))

Raises ValueError if the value is not present.

'''
print('index')
l1=[10,5,6,8,98,6,55,65,15]
print(l1.index(55))
print(l1.index(65,2,8))#from 2nd index to 8th index(not including)
#print(l1.index(65,2,7)), will give error as value not present
print(l1.index(98,1))#searches from index 1 to all over


#===========================================================================

#8.count
'''
Return number of occurrences of value
'''
print('\n')
print('count')
l1=[10,20,30,10,50,60,10]
print(l1.count(10))
print('\n')

#===========================================================================

#9.reverse
'''
returns reversed list
'''
print('reverse')
l1=[1,2,3,4,5]
l1.reverse()
print(l1)
print('\n')

#===========================================================================

#10. sort
'''
sorts the list according ascending order, lower to higher by default.

sort does not require any parameter, however it can take two parameters
syntax:list_name.sort(key=…, reverse=…) – it sorts according to user’s choice
remember: key takes function infront of it, e.g key=int

if reverse value is given as True, then sorts it in descending order.
sort is more fast than sorted

sort changes the original list, thus instead of sort their is another function
called as sorted that does not changes the original data.
sorted can be used with any iterables like string, list, tuple etc.
sorted always throws list at o/p
'''
print('\n')
print('sort')
l1=[1,20,60,68,56,26]
l1.sort()
print(l1)
l1=[1,20,60,68,56,26]
l1.sort(reverse=True)#sort the list in descending order
print(l1)

#sorted
print('\n')
print('sorted')
l1=[1,20,60,68,56,26]
print(sorted(l1))
print(sorted(l1,reverse=True))#before this no need assign l1 again

print(sorted('abhishek'))

#use of key in sorted
l1=(str(x) for x in range(1,20))
print(sorted(l1))#sorted as per strings
l1=(str(x) for x in range(1,20))
print(sorted(l1,key=int))#to sort as per numbers we can provide key=int

#best use of sorted method in multiple program list.py file
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''
miscllaneous methods like sum, min, max, + operator and * operator
'''

# + operator
print('\n')
print('+ operator')
l1=[10,20,30]
l2=[40,50,60]
print(l1+l2)

# * operator
print('\n')
print('* operator')
l1=[10,20,30]
print(3*l1)#or l1*3 any way







