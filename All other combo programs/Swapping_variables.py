#swapping variables using third variable

a=100
b=50
c=a
a=b
b=c

print('value of a:',a)
print('value of b:',b)

#swapping variable without using third variable

a=100
b=50
a=a+b
b=a-b
a=a-b

print('value of a:',a)
print('value of b:',b)

#and
a=100
b=50
a=a*b
b=a/b
a=a/b

print('value of a:',int(a))
print('value of b:',int(b))

#using simultaneous assignement
a=100
b=50
a,b=b,a

print('value of a:',a)
print('value of b:',b)

