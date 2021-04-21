#eval() in python

#eval calculates expression inside the parantheses with braces removed
#eval function takes string inside the braces, and evaluate the expression
#if we provided int as string e.g. '100' then it print int part
#we may need to import eval from math

print(eval('100'))
print(type(eval('100')))
print('\n')

print(eval('60+58'))
print(type(eval('60+58')))

print('\n')
print(eval('[1,2,3,4]'))
print(type(eval('[1,2,3,4]')))

'''
eval cannot take alphabets inside string

print('\n')
print(eval('abhi'))
print(type(eval('abhi')))
'''
print('\n')
exp=input('enter expression in terms of x as (x*x)+2:')
x=int(input('enter value of x:'))

print('value of y:',eval(exp))
