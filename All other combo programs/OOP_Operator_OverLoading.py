#OOP_Operator_Overloading(Polymorphism):
#***************************************

'''
let's say for addition operation, when we do addition of two integers then
int class ka __add__ method call hota hai, similaraly when we do
add operation on two string, then str class ka __add__ method call hota hai.


in this way , for different operation, different methods from respective classes
are called

 for e.g.. addition -->__add__
 substraction --> __sub__
 multiplication--> __mul__
 etc.

 when we are doing a+b means addition of two objects a and b,

 let's take example as below
'''

a=5
b=10
print(a+b)
print(int.__add__(a,b))

c='sukany'
d='abhi'
print(str.__add__(c,d))

'''
so in above exmple we adding two objects a and b of int class and
c and d of str class.

addition was possible here beacause both these classes have __add__
method, which gets called during execution.


now when we define our own class and create two objects from it
and do addition operator in them, then if our class don't have
__add__ method error will be displayed as below

unsupported operand type(s) for +: 'Student' and 'Student'

i.e. two objects from student class don't know about + operation
'''


#try running below code
'''
class Student:
    def __init__(self,marks):
        self.marks=marks

s1=Student(10)
s2=Student(20)
print(s1+s2)
'''

#corrected program with inclusive of add method inside class
'''
syntax: __add__(self,x)
add method takes two arguments, self and x

so while calling s1+s2, s1 goes as a self and s2 goes as x inside
add method
'''


class Student:
    def __init__(self,marks):
        self.marks=marks
    def __add__(self,other):
        return self.marks+other.marks

s1=Student(10)
s2=Student(200)
print(s1+s2)

'''
here we have defined __add__ method inside student class, so s1s+s2
works fine now.

instead of + operator in (return self.marks-other.marks), if we put
-ve sign then add method will start working as substraction,

this whole concept of introducing own add method, and changing its
behaviour (sub instead of add) is called operator overloading.


**so we can say that operator overloading can be done by method overriding,
as we are overrding system's class __add__ method by our own __add__
method(imp statement)
'''

#*************************************************************************
#Magic Methods/Dunder Methods:
'''
methods which are starting and ending with double underscore are called
as magic methods or dunder methods

they are called magic methods because, without calling them they are get
called, like __init__, __add__, __sub__ etc.
'''