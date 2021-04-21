#Ternary Operators or Conditional Expressions
#Ternary operator is basically conditional expression

'''
syntax:
[on_true] if [expression] else [on_false]
'''
#================================================================

#Example-1

x,y=5,6
print(x if x>y else y)


#================================================================
#Example-2
#By surrounding conditional expressions inside paranthesis, we can
#evaluate it first

a=b=50
print(1+(a if a>b else b)+2)

#================================================================
#Example-3
#Implementing ternary operator using Tuples
# (if_test_false,if_test_true)[test]
p,q=10,20
print((q, p) [p < q])

#===============================================================
#Example -4
#Implementing ternary operator using dictionary

a=15
b=12
print({True: a, False: b} [a < b])

#==============================================================
#Example -5
#Nested Ternary Operator

a=100
b=50
print('a and b are equal' if a==b else 'a is greater than b' if a>b else 'b greater than a')

'''this is similar to
if a!=b:
    if a>b:
        print('a is greater than b'
    else:
        print('b is greater than a'
else:
    print('a and b are equal')

'''


