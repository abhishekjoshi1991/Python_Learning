#set and their methods

'''
it is unordered collection of unique elemets(non duplicated)
it can be defined using set() function
set is immutable as per indexing and slicing but we can add or remove
elements from it

empty set can be formed by set() fucntion
{} means dictionary and not a set

'''

#==============================================================================
#creating a set
#==============================================================================

#1. using string
print(set('name'))#will give unordered strings of individual elements from string

#2.set from list
print(set([1,2,3,4,5,6]))

#3.empty set
print(set())


#==============================================================================
#set methods
#==============================================================================

#1. Union:
'''
gives elements from both set A and B without duplication
it returns the set
it returns the copy of set1 if no parameter is passed inside brackets
syntax--> s1.union(parameter)
inside parameters any number of set can be given
also parameter can be list, tuple, string, int

it does not change original set, hence throws o/p in shell
'''

print('\n')
print('o/p of union method')
s1={1,2,3,4,5}
s2={5,6,7,8}
s3={5,8,9,10}
print(s1.union(s2))
print(s1.union())#returns copy of set1
print(s1.union(s2,s3))#combines three sets
print(s1.union('abhi'))#parameter as a string

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#2. intersection:
'''
gives elements common elements from both set A and B
it returns the set
it returns the copy of set1 if no parameter is passed inside brackets
syntax--> s1.intersection(parameter)
inside parameters any number of set can be given
also parameter can be list, tuple, string, int
it does not change original set, hence throws o/p in shell
'''
print('\n')
print('o/p of intersection method')
s1={1,2,3,4,5}
s2={5,6,7,8}
s3={5,8,9,10}
print(s1.intersection(s2))
print(s1.intersection())#returns copy of set1
print(s1.intersection(s2,s3))#no result as no common element

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#3. add
'''
to add element to set
only one element can be added at a time
we can add string, tuple, int to set
but we can not add list and set to set, as list is mutable
multiple elements can be added to set using loops
print(s1.add()) will give none

it changes original set hence does not throw o/p in shell
'''

print('\n')
print('o/p of add method')
s1={1,2,3,4,5}
s1.add(10)#int addition
s1.add((10,20))#tuple addition
s1.add('abhi')#string will be added as single entity as single element
#s1.add([10,20,30]), can not add list to set
print(s1)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#4. update
'''
it is used to add multiple elements to set
syntax: s1.update(iterables)
*iterables can be set, list, string, tuple
it can not take int as parameter

it unpacks the elements from iterables and add one by one to set in any order

it changes the original set hence does not throw o/p in shell
'''

print('\n')
print('o/p of update method')
s1={10,20,30,40,50}
s1.update([60,70,30])#iterable as a list
s1.update('abhi')#iterable as a string
#s1.update(100)-->iterable as a int, will give error
print(s1)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#5. remove and discard
'''
remove methods removes the specified element from set, if element is not
present in set then gives key error.

whereas discard method work same to remove method but does not throws key
error
remove and discard method changes original set, hence does not throw value
'''

print('\n')
print('o/p of remove and discard method')
s1={10,20,30,40,50}
s1.remove(10)
#s1.remove(500)--> gives key error
s1.discard(500)#--> does not give key error
print(s1)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#6. pop
'''
pop method removes random element from set and returns its value

syntax: s1.pop()

it does not take any argument
'''
print('\n')
print('o/p of pop method')
s1={10,20,30,40,50}
print(s1.pop())
print(s1)


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#7. clear
'''
removes all elements from the set, gives empty set after printing
'''
print('\n')
print('o/p of clear method')
s1={10,20,30,40,50}
s1.clear()
print(s1)


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 8. differnce
'''
let
A={10,20,30,40,80}
B={40,20,80,50,60,70}
then
A-B means elemets present in A but not in B
B-A meanns elements present in B but not in A

it creates new set at output
'''
print('\n')
print('o/p of difference method')
A={10,20,30,40,80}
B={40,20,80,50,60,70}
print(A-B)#element 10 and 30 prsent in A but not in B
print(B-A)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 9. differnce_update
'''
this method is similar to A-B but it changes value of A equal to A-B
'''

print('\n')
print('o/p of difference_update method')
a={10,20,30,40,80}
b={40,20,80,50,60,70}
a.difference_update(b)
print(a)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 10.symmetric_difference
'''
this method prints all the elements except common elements from both set
as a new set
'''
print('\n')
print('o/p of symmetric_difference method')
a={10,20,30}
b={30,40,50}
print(a.symmetric_difference(b))#it have not printed 30

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 11.symmetric_difference_update

'''
this method same as above, but result is saved in original set for which we
are called this method
'''
print('\n')
print('o/p of symmetric_difference_update method')
a={10,20,30}
b={30,40,50}
a.symmetric_difference_update(b)#method is called for a, hence a is updated
print(a)#a is changed
print(b)#b is not changed


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 12. issubset
'''
return true for a.issubset(b) if all elemets from set a present in set b
'''
print('\n')
print('o/p of issubset method')
a={10,20,30,40,50}
b={10,20,30,40,50,60,70,80}
print(a.issubset(b))

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 13.issuperset
'''
return true for a.issuperset(b) if all elemets from set b present in set a
in other word set a occupies all elements from set b
'''
print('\n')
print('o/p of issuperset method')
a={10,20,30,40,50}
b={10,20,30,40,50,60,70,80}
print(a.issuperset(b))
print(b.issuperset(a))#all elements of b present in a

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 14. isdisjoint
'''
returns True if two sets don't have any common elements
'''
print('\n')
print('o/p of isdisjoint method')
a={10,20,30,40,50}
b={60,70,80}
print(a.isdisjoint(b))






