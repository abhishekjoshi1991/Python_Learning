#operators in python
#1.arithmetic operators-->+,-,*,/,%,**,//

print('result of arithmetic operators')
a=9
b=2
print(a+b)
print(a-b)
print(a*b)
print(a/b)#always gives float as o/p
print(a%b)
print(a**b)
print(a//b)

#============================================================
# 2.Bitwise Operator
# see video https://www.youtube.com/watch?v=PyfKCvHALj8
"""
&       Bitwise AND
|	Bitwise OR
~	Bitwise NOT
^	Bitwise XOR
>>	Bitwise right shift
<<	Bitwise left shift
"""

#============================================================
# 3.Comparison Operator-->==,!=,>,<,<=,>=
print('\n')
print('result of comparison operators')
a=20
b=10
print(a==b)#equal to: true if both operands are equal
print(a!=b)#Not equal to - True if operands are not equal
print(a>b)
print(a<b)
print(a<=b)
print(a>=b)

#============================================================
#4.Logical Operators-->and, or ,not

"""
and	Logical AND: True if both the operands are true
or	Logical OR: True if either of the operands is true
not	Logical NOT: True if operand is false
"""
print('\n')
print('result of logical operators')
a = True
b = False
print(a and b) 
print(a or b) 
print(not a) 

#============================================================
#5.Assignment Operators-->=,+=,-=,*=,/=,%=,//=,**= and other bitwise assignment operator

#a=10, = is assignment operator
#a+=b --> a=a+b
#a-=b --> a=a-b
#a*=b --> a=a*b
#a/=b --> a=a/b
#a%=b --> a=a%b
#a//=b --> a=a//b
#a**=b --> a=a**b

#============================================================
#6. Special operators in python
#identity operator-->is and is not
#both are used to check if two values are located on the same part of the memory.
# we can check memory location using id() function

print('\n')
print('results of identity operators')
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]
print(x1 is y1)
print(x2 is y2)
print(x3 is y3)

#x3 and y3 are lists. They are equal but not identical. It is because the interpreter
#locates them separately in memory although they are equal.


#is operator returns true only when
#1. Integer numbers between -5 and 256
#2. Strings that contain ASCII letters, digits, or underscores only


a=-5
b=-5
print(a is b)

p=-6
q=-6
print(p is q)

x1=257
y1=257
print(id(x1))
print(id(y1))
print(x1 is y1)

l='hello!'
m='hello!'
print(l is m)


