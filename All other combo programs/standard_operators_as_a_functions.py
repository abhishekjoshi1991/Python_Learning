#Standard operators as a functions
#after importing operator module set of fuctions related to operators are imported


'''
methods starts and ends with double underscore are called as dunder or magic
methods and mostly used in operator overloading
'''

import operator

#to check all attributes inside operator module---use
print(dir(operator))
#====================================================================================
'''
operator.lt(a,b)   or   operator.__lt__(a,b)--> a<b
operator.le(a,b)   or   operator.__le__(a,b)--> a<=b
operator.eq(a,b)   or   operator.__eq__(a,b)--> a==b
operator.ne(a,b)   or   operator.__ne__(a,b)--> a!=b
operator.ge(a,b)   or   operator.__ge__(a,b)--> a>=b
operator.gt(a,b)   or   operator.__gt__(a,b)--> a>b
operator.abs(a)    or   operator.__abs__(a)--> returns abs of a
operator.add(a,b)   or   operator.__add__(a,b)--> a+b
operator.sub(a,b)   or   operator.__sub__(a,b)--> a-b
operator.mul(a,b)   or   operator.__mul__(a,b)--> a*b
operator.truediv(a,b)   or   operator.__truediv__(a,b)--> a/b
operator.floordiv(a,b)   or   operator.__floordiv__(a,b)--> a//b
operator.pow(a,b)   or   operator.__pow__(a,b)--> a**b
operator.mod(a,b)   or   operator.__mod__(a,b)--> a%b
operator.neg(a)   or   operator.__neg__(a)--> returns negative value
'''
#====================================================================================
'''
operator.concat(a,b)   or   operator.__concat__(a,b)--> 'a+b'
operator.contains(a,b)   or   operator.__contains__(a,b)--> outcome of b in a
operator.countOf(a,b) --> number of occurances of b in a
operator.delitem(a,b)   or   operator.__delitem__(a,b)--> remove value
of a at index b

operator.getitem(a,b)   or   operator.__getitem__(a,b)--> return value of a
at index b

operator.indexOf(a,b) --> return index of first occurance of b in a

'''

a='abhi'
b='joshi'
print(operator.__concat__(a,b))
print('\n')

a=[10,2,0,30,40]
print(operator.__contains__(a,30))
print('\n')

x=[1,2,3,4,5,7,5,6,8,1]
print(operator.countOf(x,1))
print('\n')

x=[1,2,3,4,5,7,5,6,8,1]
operator.__delitem__(x,2)#removes value at index 2
print(x)
print('\n')

x=[1,2,3,4,5,7,5,6,8,1]
print(operator.__getitem__(x,6))#returns value at index 6

#=====================================================================================
'''
operator.is_(a,b) --> test objects identity
operator.is_not(a,b) --> returns a is not b
operator.and_(a,b)  or operator.__and__(a,b) -->bitwise and value
operator.or_(a,b)  or operator.__or__(a,b) -->bitwise or value
'''

#=====================================================================================

#Slicing, Slice Deletion, Slice Assignment

a=[1,2,3,4,5,6,7,8,9,10]
print(operator.getitem(a,slice(3,6)))#slicing

operator.delitem(a,slice(3,6))#slice deletion
print(a)

a=[1,2,3,4,5,6,7,8,9,10]
operator.setitem(a,slice(3,6),('x','y','z'))#slice assignment
print(a)

#====================================================================================






















