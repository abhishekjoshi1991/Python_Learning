#in_place operators

#x+=y is equivalent to x=operator.iadd(x,y)

#in_place operators behaves differntly for mutable and immutable objects

'''
1. For immutable targets such as strings, numbers, and tuples,
the updated value is computed, but not assigned back to the input variable
'''

import operator
a='hello'
print(operator.iadd(a,' world'))
print(a) #original value of a is not changed as string is immutable
#============================================================================

'''
2.For mutable targets such as lists and dictionaries, the in-place method
will perform the update, so no subsequent assignment is necessary:
'''

s=[1,2,3,4,5]
print(operator.iadd(s,[10,20,30,40]))
print(s)#original value of s is updated due to mutability of list

#===========================================================================

'''some in_place operators are
operator.iadd(a, b)  or operator.__iadd__(a, b) --> a += b
operator.iand(a, b) or operator.__iand__(a, b) --> a &= b
operator.ifloordiv(a, b) or operator.__ifloordiv__(a, b) -->a //= b
operator.imod(a, b) or operator.__imod__(a, b) -->a %= b
operator.imul(a, b) or operator.__imul__(a, b) --> a *= b
operator.ipow(a, b) or operator.__ipow__(a, b --> a**=b
operator.isub(a, b) or operator.__isub__(a, b) --> a-=b

and many others

'''



