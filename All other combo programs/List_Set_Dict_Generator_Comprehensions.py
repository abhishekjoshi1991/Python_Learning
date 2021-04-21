#List, Set, Dict, Generator Comprehensions

#-------------------------------------------------------------
#1. List Comprehension
#-------------------------------------------------------------
'''
uses [] symbol to define

syntax: [expression for each in iterables]
syntax: [expression for each in iterables if condition]

if there is one condition it can be mentioned after for and
if there are two conditions then it has to be mentioned
before for

List comprehensions are used for creating new lists
from other iterables like tuples, strings, arrays,
lists, etc.

'''
print('\n')
print('list comprehension')
#Program-1
#Squares of numbers from 1 to 10
print([x**2 for x in range(1,11)])

#Program-2
#squares of even numbers from 1 to 10
print([x**2 for x in range(1,11) if x%2==0])

#Program-3
#squares of even numbers and cubes of odd nums from 1 to 10
print([x**2 if x%2==0 else x**3 for x in range(1,11)])

#Program-3
#to print hello world many times as per len of string
print(['hello' for x in 'ethans'])

#Program-4
#[11,33,50]-->113350
l1=[11,33,50]
print(int(''.join(str(i) for i in l1)))

#Program-5
#Program to print table of 5
print([i*5 for i in range(1,11)])

#Program-6
#Nested list comprehension
print([[j for j in range(1,5)] for i in range(0,3)])

#Program-7
#list comprehension with lambda
#to display table of 6
print(list(map(lambda x:x*6,[x for x in range(1,11)])))

#Program-8
#Reverse each string in tuple
print([i[::-1] for i in ('Geeks', 'for', 'Geeks')])

#-------------------------------------------------------------
#2. Set Comprehension
#-------------------------------------------------------------
'''
gives u ique elements and uses {} brackets
'''
print('\n')
print('set comprehension')
l1=[1,2,3,2,2,3,5,3,5,3,5]
print({x**2 for x in l1})

#-------------------------------------------------------------
#3. generator Comprehension
#-------------------------------------------------------------
'''
uses () brackets.
it throws the object at o/p, data can be genereated through
it whenever required by iterating over it or type cast it
into suitable data type
'''
print('\n')
print('generator comprehension')
print((x**2 for x in range(1,10)))#throws object
a=(x**2 for x in range(1,10))
print(list(a))

#-------------------------------------------------------------
#4. dict Comprehension
#-------------------------------------------------------------
'''
it also uses {} brackets but it contains two expression
one for key and other for value.

two expressions are seperated by colon:
syntax:{expression1:expression2 for each in iterable}
'''
print('\n')
print('dict comprehension')
print({x:x**2 for x in range(1,11)})

#program to print {1:'A',2:'B'...}
print({x:chr(x+64) for x in range(1,27)})

#Program to inverse the given dict
d1={1:'A',2:'B',3:'C',4:'D'}
print({y:x for x,y in d1.items()})
print({d1[i]:i for i in d1})

#Program to find occurances of elements from list
l=[1,2,2,3,4,2,2,3,3,4,4,5,6]
print({i:l.count(i) for i in l})#as duplicated keys can not be present

#optimized program of above
print({i:l.count(i) for i in set(l)})
