#------------------------------------------#
# Functions_Zip,Map,Filter,Reduce,Lambda   #
#------------------------------------------#
'''
Basic difference:
map-->we have 10 values and we get 10 values
reduce-->we have 10 values we get 1 value or one object
filter--> we have 10 value we get values based on some condition
'''

'''
all these functions except reduce gives object at o/p, hence we need to
iterate over it or type cast it to suitable format
'''
#=============================================================================
# zip    
#---------
'''
syntax: zip(*iterables) as many as possible iterables it can take

it combines the iterables till smallest length of iterable
'''
print('zip')
l1=[1,2,3,4,5]
l2=[10,20,30]
l3=['a','b','c','d','e','f']
print(list(zip(l1,l2)))#it will zip till smallest length of iterable here l2
print(list(zip(l2,l3)))
print(dict(zip(l2,l3)))

#=============================================================================
# Map    
#---------

'''
syntax:map(function,*iterables)#function can be built-in or user defined
we can have multiple iterables at a time

map will pass the function over all the iterables

map also throws object at o/p
'''
print('\n')
print('map')
def sq(num):
    return num**2
print(list(map(sq,[1,2,3,4,5])))
print(list(map(sq,range(1,21))))

def mysum(a,b):
    return a+b
print(list(map(mysum,range(1,11),range(11,21))))#it will pick one one element from
#both iterables and make sum of it

#program to print maximum as per index position from two lists
l1=[1,3,2,3,5,6,7]
l2=[33,4,5,6,7,3,2]
print(list(map(max,zip(l1,l2))))#here we passed buit in function 'max'

#Program to make dict, where keys are strings from list and values are len of strings
z=['abc','pq','stjf','dajas','afs']
print(dict(zip(z,map(len,z))))

#Program to print {1:'A',2:'B'.....}
print(dict(zip(range(1,27),map(chr,range(65,65+26)))))

#Program to join integers in a list
#[11,33,10]-->113310
l=[11,33,10]
print(int(''.join(map(str,l))))

#Program to convert string of numbers into list
#'1,2,3,4,5'-->[1,2,3,4,5]
ip='1,2,3,4,5'
print(list(map(int,ip.split(','))))

#Program
#[('G','E','E','K','S'),('F','O','R'),('G','E','E','K','S')]->['GEEKS','FOR','GEEKS']
b=[('G','E','E','K','S'),('F','O','R'),('G','E','E','K','S')]
print(list(map(''.join,b)))

'''
as observed above, we always need to defined overhead function before using
map, this need of overhead function can be eliminated using lambda function below
'''

#=============================================================================
# lambda    
#---------

'''
it is an anonymous function (without name)that generally used with map,
reduce or filter
instead using overhead function, we can define lambda function inside map (or
reduce or filter)directly

general syntax:
lambda arguments:value to return(expression)

This function can have any number of arguments but only one expression,
which is evaluated and returned.
'''
print('\n')
print('lambda')
print(list(map(lambda x:x**2,[10,20,30])))

print(list(map(lambda a,b:a+b,range(1,11),range(11,21))))

#program to print maximum as per index position from two lists
print(list(map(lambda x,y:max(x,y),[1,3,2,3,5,6,7],[33,4,5,6,7,3,2])))
print(list(map(lambda x,y:x if x>y else y,[1,3,2,3,5,6,7],[33,4,5,6,7,3,2])))


#program to make squares of even nums only

#=============================================================================
# reduce    
#---------

'''
need to be imported first from functools
syntax: reduce(func,sequence)

it applies the function to all elements in sequence

working:
1. At first step, first two elements of sequence are picked
and the result is obtained.
2. Next step is to apply the same function to the previously
attained result and the number just succeeding the second
element and the result is again stored.
3. process is repeated till no more elements are left in seq

reduce does not throw object at output
'''

print('\n')
print('reduce')
from functools import reduce
print(reduce(lambda x,y:x+y,[1,10,2,20,1,2]))

'''
explaination
x=1,y=10-->x=11
x=11,y=2-->x=13
x=13,y=20-->x=33
x=33,y=1-->x=34
x=34,y=2-->x=36
'''


#-----------------------------------------------------------------------------
'''
difference between reduce and accumulate
1. reduce() is defined in “functools” module,
accumulate() in “itertools” module.
2. reduce() returns the final value while accumulate() returns
intermediate values also in the form of list or tuple whichever
is mentioned
3. reduce(func,seq) and accumulate(seq,func)
'''
print('\n')
print('difference between reduce and accumulate')
from functools import reduce
from itertools import accumulate
l1=[1,3,4,10,4]
print(reduce(lambda x,y:x+y,l1))
print(list(accumulate(l1,lambda x,y:x+y)))

#program to find max from list using reduce
l1=[1,4,50,6,7,8,1,10]
print(reduce(lambda x,y:max(x,y),l1))
print(reduce(lambda x,y:x if x>y else y,l1))

#program for factorial using reduce
num=int(input('enter num for which fact to be calculate:'))
print(reduce(lambda x,y:x*y,range(2,num+1)))


#=============================================================================
# filter    
#---------

'''
it filters the element from seq based on some condition passed in the function

it throws object at o/p.

it tests each element of sequence to be true or not
'''
#program for numbers from 1 to 100 divisible by 7
print('\n')
print('filter')
print(list(filter(lambda x:x%7==0,range(1,101))))

#program to filter only vowels from a lsit of strings
l1=['g', 'e', 'e', 'j', 'k', 's', 'p', 'r','i']
print(list(filter(lambda x:x in ['a','e','i','o','u'],l1)))


#=============================================================================

#Program to sort the list of tuples according to second element
#of tuple
l2=[(2,5),(1,2),(4,4),(2,3),(2,1)]
print(sorted(l2))#regular way, sorts according to first index
print(sorted(l2,key=lambda x:x[1]))



#Program to find squares of even numbers from a list
l3=[1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda x:x**2,filter(lambda x:x%2==0,l3))))


#Program to sort the list using length of elements
c=['very','is','language','python','easy']
print(sorted(c,key=len))

#Program to sort the dict to find second highest marks in maths
d1={101:{'name':'arjun','marks':{'maths':85,'geo':98}},
    102:{'name':'sachin','marks':{'maths':45,'geo':68}},
    103:{'name':'ashish','marks':{'maths':75,'geo':78}},
    104:{'name':'amit','marks':{'maths':95,'geo':98}}}

print((sorted(d1.items(),key=lambda x:x[1]['marks']['maths']))[-2])

