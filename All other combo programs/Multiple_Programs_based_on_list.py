# Python Program on lists

#Program 1
'''
Write a Python program to get a list, sorted in increasing order by the
last element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
'''
a=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
a.sort(key=lambda x:x[1])
print(a)

#or
def last(n):
    return n[-1]
def checklist(t):
    return sorted(t,key=last)#key takes any func in front of it, here func last is called
t=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(checklist(t))

#==============================================================================
#Program 2
#to check list is empty or not
print('\n')
l=[]
if not l:
    print('list is empty')


#==============================================================================
#Program 3, use of sorted to sort list
    
l=['abc','pg','gket','bfjkgsnk']
print('\n')
#to sort this list by default
print(sorted(l))

#to sort list according to length of strings
print(sorted(l,key=len))

#to sort the list as per length of string in reverse order
print(sorted(l,key=len,reverse=True))

#to sort the list as per the first index value of string from list
def func(a):
    return a[1]

print(sorted(l,key=func))

#==============================================================================
#Program 4: 
'''
Write a Python program to find the list of words that are longer than n from a given
list of words or given string
'''
print('\n')
string='The quick brown fox jumps over the lazy dog'
length=3
newlist=[]
for i in string.split():
    if len(i)>length:
        newlist.append(i)
print(newlist)

#==============================================================================
#Program 5:Program to print list after removing specified elements
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow','purple']
#to remove items from index position 0,3 5.
print('\n')
new=[v for (i,v) in enumerate(color) if i not in (0,3,5)]
print(new)

#==============================================================================
#Program 6: to shuffle and print given list
from random import shuffle
print('\n')
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
shuffle(color)
print(color)

#==============================================================================
#Program 7:Generate all permutations of a list in Python
print('\n')
a=[1,2,3]
import itertools
print(list(itertools.permutations(a)))#itertools.permutations gives object at o/p ,
#hence need to typecast to list

#==============================================================================
#Program 8: Program to print differnce of two lists
#method 1 : using set function
print('\n')
l1=[1,2,3,4]
l2=[1,2,5,6]
a=list(set(l1)-set(l2))#it removes unique elements from l1 those are present in l2
print(a)
b=list(set(l2)-set(l1))#it removes unique elements from l2 those are present in l1
print(b)
print(a+b)

#method 2: using for loop
l1=[1,2,3,4]
l2=[1,2,5,6]
l3=[]
for i in l1+l2:
    if i not in l1 or i not in l2:
        l3.append(i)
print(l3)


#==============================================================================
#Program 9:Program to flatten the list

l = [[1, 2, 3], [40, 5, 6], [70], [8, 9]]#expected o/p [1, 2, 3, 40, 5, 6, 70, 8, 9]
f=[]
for i in l:
	for j in i:
		f.append(j)
print(f)

#or using itertools

l=[[2,4,3],[1,5,6], [9], [7,9,0]]
import itertools
new=list(itertools.chain(*l))#* does unpacking of list
print(new)

#==============================================================================
#Program 10: Python program to select an item randomly from a list
a=[10,20,30,40,50]
import random
print(random.choice(a))

#==============================================================================
#Program 11: Program to selected second smallest number in list
l=[2,3,5,8,0,1,2,7]
print(sorted(l)[1])

#==============================================================================
#Program 12: Program to selected second largest number in list
l=[2,3,5,8,0,1,2,7]
print(sorted(l)[-2])

#==============================================================================
#Program 13: program to get frequency of items in list
l=[10,10,10,20,20,30,30,30,30]
import collections
print(collections.Counter(l))
