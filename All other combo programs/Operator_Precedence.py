#operator precedence in python
'''
Operators	Meaning
()	        Parentheses
**	        Exponent
+x, -x, ~x	Unary plus, Unary minus, Bitwise NOT
*, /, //, %	Multiplication, Division, Floor division, Modulus
+, -	        Addition, Subtraction
<<, >>	        Bitwise shift operators
&	        Bitwise AND
^	        Bitwise XOR
|	        Bitwise OR
==, !=, >, >=, <, <=, is, is not, in, not in	Comparisons, Identity, Membership operators
not	        Logical NOT
and	        Logical AND
or	        Logical OR

'''
=============================================================================================
'''Associativity of Python Operators

When two operators have the same precedence, associativity
helps to determine the order of operations.
Associativity is the order in which an expression is evaluated that
has multiple operators of the same precedence.
Almost all the operators have left-to-right associativity.
(except ** operator has right to left associativity) e.g 5**2**3 '''

print(5 * 2 // 3)
print(5 * (2 // 3))

============================================================================================
'''
Non associative operators

For example, x < y < z neither means (x < y) < z nor x < (y < z).
x < y < z is equivalent to x < y and y < z, and is evaluated from left-to-right.
'''

===========================================================================================

# Precedence of or & and
meal = "fruit"

money = 0

if meal == "fruit" or meal == "sandwich" and money >= 2:
    print("Lunch being delivered")
else:
    print("Can't deliver lunch")


# Precedence of or & and using parantheses
meal = "fruit"

money = 0

if (meal == "fruit" or meal == "sandwich") and money >= 2:
    print("Lunch being delivered")
else:
    print("Can't deliver lunch")
