#base 2 and base 10 concept, ASCII code-->for type conversion
#----------------------------------------------------------------------------
#Type conversion
#list(string) will give list of all string iterables
print(list('abhishek'))

#dict([1,2,3,4]) is not possible as dict requires keys and values
#dict((1,2,3,4)) is also not possible

#only structure which is eligible to convert to dict is
print(dict([(1,2),(3,4)])) #i.e. list of tuples
print(dict(((1,2),(3,4)))) #i.e tuple of tuples
#----------------------------------------------------------------------------
#base 2 stands for binary system which is formed by only two numbers (0,1)

#base 10 stands for decimal system which uses base as 10 for (0 to 9) numbers

'''
Number  Binary
0	0
1	1
2	10
3	11
4	100
5	101
6	110
7	111
8	1000
9	1001
10	1010
'''

#int() function syntax
#int(x,10), here 10 means base 10, default base is 10 unless specified
#when base is given that means x must be in str

print(int('100',10))

#when base not given, it is expected to pass str with numbers only
print(int('200'))

#when base 2 is given, binary form of number converted to number, means
print(int('1000',2))#here 1000 stands for number 8

#we cannot convert this string of this type to int
#print(int('h500'))-->invalid literal with base 10

'''
in short
when we take base as 2, given string must be valid binary code of any number

when we take base as 10, given string must be numbers from 0 to 9 only
'''
#-----------------------------------------------------------------------------

#ASCII Table

#chr(ASCII code)=Letter
#ord(letter)=ASCII code


'''
Letter	ASCII  Letter	ASCII
        Code	        Code
        
a	97	A	65
b	98	B	66
c	99	C	67
d	100	D	68
e	101	E	69
f	102	F	70
g	103	G	71
h	104	H	72
i	105	I	73
j	106	J	74
k	107	K	75
l	108	L	76
m	109	M	77
n	110	N	78
o	111	O	79
p	112	P	80
q	113	Q	81
r	114	R	82
s	115	S	83
t	116	T	84
u	117	U	85
v	118	V	86
w	119	W	87
x	120	X	88
y	121	Y	89
z	122	Z	90

0       48
1       49
2       50
3       51
4       52
5       53
6       54
7       55
8       56
9       57

'''
#-------------------------------------------------------------------------------       
