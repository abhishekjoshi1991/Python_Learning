# Tuples and it's methods:
'''
tuple is collection of different objects(strings, int, list, etc.)
tuple is ordered sequence
tuples are immutable i.e. does not support item assignment

Values of a tuple are syntactically separated by ‘commas’.
Although it is not necessary, it is more common to define a tuple
by closing the sequence of values in parentheses.
This helps in understanding the Python tuples more easily.
this means a=1,2,3,4 is also tuple

single value is tuple can be specified with use of trailing comma
i.e. a=(1,) is tuple and a=(1) is int

we can not add or remove item from tuple, but tuple can be deleted using
del operator
'''
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#creating a tuple:
#1. using in built tuple function on list
#tuple() method can convert any iterable to tuple

a=[1,2,3,4]
print(tuple(a))


#2. using in buit function on string,
# tuple will be created of individual elements from string
print('\n')
a='abhishek'
print(tuple(a))

#3. tuple can be created with multiple objects
print('\n')
a=([1,2],'abhi',(10,20,30),10.5)
print(a)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# accessing a tuple:
'''tuple (elements in tuple) can be accessed with unpacking or indexing.
In unpacking of tuple number of variables on left hand side should be equal to
number of values in given tuple.
'''
#accessing with help of indexing
print('\n')
a=(10,20,30,'ethans')
print(a[3][2])

#accessing with help of unpacking
print('\n')
a=(10,20,30)
x,y,z=a
print(x)
print(y)
print(z)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# concatenation of tuples:
'''
method of joining two or more tuple using + operator
'''
print('\n')
t1=(1,2,3)
t2=('a','b','c')
print(t1+t2)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# slicing of tuples:can be done same as list

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#deleting a tuple:
'''
tuple can be deleted using del keyword, whole tuple will be deleted

a=(1,2,3)
del(a)
print(a)#will give error that a is not defined
'''

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#tuple methods:

'''
there are only two methods mainly available with tuple, index and count.
other secondary methods are min, max, sum, sorted etc.
'''
#1. count
'''
counts number of occurences of element within tuple.
this method throws value in shell window
'''
print('\n')
b=(10,20,30,40,550,40,60)
print(b.count(40))

#2.index
'''
returns index position for first occurance of element
syntax: t.index(value,start,end)
'''
print('\n')
b=(10,20,30,40,550,40,60,40)
print(b.index(40))


#3. sorted
'''
sorts the tuple in ascending order by default, same as that
of list.
sorted method does not change original tuple(sort method not
available with tuple as it is immuatable)
if reverse=True is given then sorts according to descending order
'''
print('\n')
a=(40,20,10,30,50,60)
print(sorted(a))
print(sorted(a,reverse=True))
