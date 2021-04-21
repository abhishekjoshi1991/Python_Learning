#Dictionary and its methods

#==============================================================================
'''
dictionary has identifier called as 'Keys' (same as index position of list)
to fetch values

dictionary can be indexed based on keys

dictionary values are mutable that means we can change the value at
particular key and not keys are immutable

dictionary is unordered structure

dictionary have uniques keys, if we assign two keys with same name then,
it will fetch recent one

keys are case sensitive

keys are taken as immutable objects like int,float,str,tuple
but for values any object can be taken

values can be duplicated but keys must be unique
'''
#==============================================================================

#------------------------------------------------------------------------------
#Creating a dictionary
#------------------------------------------------------------------------------
'''
empty dict can be created using empty curly braces {}
dict can also be formed using dict keyword
only structure which is capable of converting to dictionary is list of tuple or
tuple of tuples or list of list, but they must in pair (k,v)
'''
d=dict([(10,20),(30,40)])
print(d)



#------------------------------------------------------------------------------
#dictionary methods
#------------------------------------------------------------------------------

#1. keys()
'''
it returns all the keys from dictionary.
keys can not be fetched using indexing method as in list

it does not returns pure list of keys though it look like list
if we check type of d.items() then it won't be list

as it does not throws pure list hence we can not call 'd.keys()[]' particular
index, it will show not subscriptable
'''

print('\n')
print('o\p of keys() methods')
d1={1:'A',2:'B',3:'C'}
print(d1.keys())

#------------------------------------------------------------------------------

#2. values()
'''
it returns all the values from dictionary.

it also does not returns pure list of values though it look like list

as it does not throws pure list hence we can not call 'd.values()[]' particular
index, it will show not subscriptable
'''
print('\n')
print('o\p of values() methods')
d1={1:'A',2:'B',3:'C'}
print(d1.values())

#------------------------------------------------------------------------------

#3.items()
'''
it returns tuple of key,values inside list, not this list is not a pure list

as it does not throws pure list hence we can not call 'd.items()[]' particular
index, it will show not subscriptable
'''

print('\n')
print('o\p of items() methods')
d1={1:'A',2:'B',3:'C'}
print(d1.items())

'''
we can iterate over the d.keys(), d.values() and d.items()
if we pass single iterator in for loop for d.items() then it will print
key,value pair as a tuple

and if we pass two iterators (i,j) then it will seperately give keys and values
'''

print('\n')
print('o\p of iterating over d.items()')
d1={1:'A',2:'B',3:'C'}
for i in d1.items():
    print(i)

print('\n')

for i,j in d1.items():
    print(i, j)

#------------------------------------------------------------------------------

#4. copy()
'''
it returns shallow copy of existing dictionary, shallow copy means changes
made in any dictionary after copy method will not be reflected in other

copy() method does not take any parameter
'''

print('\n')
print('o\p of copy() methods')
d1={1:'A',2:'B',3:'C'}
d2=d1.copy()
print(d1)
print(d2)

#let's make changes in either d1 or d2 now
d1.pop(1)
print(d1)
print(d2)#changes doesn't take place in d2


'''now instead of copy method if we have used assignment operation '=' then
it will be considered as deep copy i.e. changes will be affcted in both dicts
'''

#------------------------------------------------------------------------------

#5. clear()
'''
removes all items from dictionary
'''
print('\n')
print('o\p of clear() methods')
d1={1:'A',2:'B',3:'C'}
d1.clear()
print(d1)

'''
difference between clear and {} dictionary

when we assign {} to dictionary (or variable) a new dictionary is created
and new reference is assigned to it whereas,

if clear the dictionary then actual dictionary content is removed and all
other refernces pointing to that dictionary also becomes empty
'''
print('\n')
print('o\p of difference between clear() and {} methods')
d1={1:'A',2:'B',3:'C'}
d2=d1
d1.clear()
print('o/p after removing items from d1')
print(d1)
print(d2)

d1={1:'A',2:'B',3:'C'}
d2=d1
d1={}
print('o/p after assigning {} to d1')
print(d1)
print(d2)


#------------------------------------------------------------------------------

#6. pop()

'''
removes  and returns (print) the value associated with key passed
syntax: d.pop(key,def)
#def is default value to return if key not found

if default value is not given then it will throw key error

'''
print('\n')
print('o\p of pop() methods')
d1={1:'A',2:'B',3:'C'}
print(d1.pop(1))#it will return value associated with key
print(d1)
print(d1.pop(50,'Z'))#key 50 not present in d1 hence it will print def value 'z'
#print(d1.pop(50)), it will throw key error


#------------------------------------------------------------------------------

#7. popitem()
'''
it removes and returns(as a tuple) last key value pair (in python 3.7 onwards),
in before version it removes random key value pair

popitem does not take any parameter

'''
print('\n')
print('o\p of popitem() methods')
d1={1:'A',2:'B',3:'C'}
print(d1.popitem())

#------------------------------------------------------------------------------

#8. get()

'''
accessing elements from a list
1. using key as a index
d1={10:'A',20:'B',30:'C'}
print(d1[10])-->it will give value associated with it

but d1[40]--> will throw key error,
to element this error get method is used

get method returns the value associated with given key, if key present in dict
If key does not present in dict, then it will return none if default value
is not provided as a parameter
if default value is provided in parameter then it will print that value

syntax: d.get(key,default)
'''

print('\n')
print('o\p of get() methods')
d1={1:'A',2:'B',3:'C'}
print(d1.get(3))
print(d1.get(4,'D'))#default value will be printed here

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
'''
Hint: Using del keyword, we can delete entire dictionary or we can delete
specific key value pair also
e.g. del d1[10]
'''
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------

#9. setdefault()
'''
it returns the value associated with passed key if key present in it(like get())

if key does not present, then it will assign None value to that key, if no
default value is provided as a parameter

but if default is provided, then it will assign that value to that key

syntax: d.setdefault(key,default)
'''
print('\n')
print('o\p of setdefault() methods')
d1={10:'A',20:'B',30:'C'}
print(d1.setdefault(30))
d1.setdefault(40,'D')
print(d1)
d1.setdefault(60)
print(d1)#set None value to key 60

#if key is present and default value also given, then it ignors default value
d1.setdefault(10,'Z')
print(d1)

#------------------------------------------------------------------------------

#10. update()
'''
this method updates the dictionary with elements from another dictionary or
iterable structure of key:value

syntax: d.update(other dict or iterable structure)

'''

print('\n')
print('o\p of update() methods')
d1={10:'A',20:'B',30:'C'}
d2={10:'abc'}

d1.update(d2)#for key 10 new value is assigned from dict d2
print(d1)

d1.update({40:'D',50:'E'})#updating with dict as a parameter
print(d1)

d1.update(((60,70),(80,90)))#updating with suitable structure
print(d1)

#structure can be any list of list, tuple of tuple or list of tuples.

#------------------------------------------------------------------------------

#11. fromkeys()
'''
syntax: d.fromkeys(iterable,value=None)
Create a new dictionary with keys from iterable and key's value set to value
default value is none if not provided
'''
print('\n')
print('o\p of fromkeys() methods')
a=dict.fromkeys([10,20,30],100)
print(a)

b=dict.fromkeys((10,20,30,40))#no value is given
print(b)

c=dict.fromkeys('string',[10,20])
print(c)











