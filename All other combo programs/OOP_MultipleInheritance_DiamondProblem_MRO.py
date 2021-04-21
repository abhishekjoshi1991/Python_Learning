#**************************************************
#Multiple inheritance (diamond problem in python):*
#**************************************************

#multiple inheritance is when, single class in inheriting from two or more
#classes

'''
Diamond Problem:

                          class A
                         /       \
                        /         \
                    class B     class C
                        \         /
                         \       /
                          class D


It refers to an ambiguity that arises when two classes Class B and Class C
inherit from a superclass Class A and class Class D inherits from both
Class B and Class C. If there is a method “m” which is an overridden method
in one of Class B and Class C or both
then the ambiguity arises which of the method “m” Class D should inherit

that means method in class A is overridden in class B and Class C, then
while calling that method for object from class D, then which method
that object must call

for example
'''

#1. method is overridden in both classes B and C, and D don't have method

print('method overridden in both classes')
class A:
    def func1(self):
        return 'i am in class A'

class B(A):
    def func1(self):
        return 'i am in class B'

class C(A):
    def func1(self):
        return 'i am in class C'

class D(B,C):#let's say class D don't have any method
    pass
#create object from class D
d1=D()
print(d1.func1())#here question is what it must print???

'''
here above when we call d1.func1(), python checks for func1 method
present in class D or not, if it is not present then it checks in
immediate parent class as per order passed in D(B,C) i.e. firstly
in B, here it finds method in B class, so output will be 'i am in class B'

if we have given order as class D(C,B), then python first checks in class C
in that case output will be 'i am in class C'
'''



#2. method is overridden in both classes B and C, and D have that method

print('\n')
print('method overridden in both classes, D have same method')
class A:
    def func1(self):
        return 'i am in class A'

class B(A):
    def func1(self):
        return 'i am in class B'

class C(A):
    def func1(self):
        return 'i am in class C'

class D(B,C):
    def func1(self):
        return 'i am in class D'
#create object from class D
d1=D()
print(d1.func1())

'''
here above, method is present in class D itself, hence it will not go 
to parent or grandparent class, hence output will be 'i am in class D'
'''


#3. method is overridden in class C, only and D don't have that method

print('\n')
print('method overridden in class C only')
class A:
    def func1(self):
        return 'i am in class A'

class B(A):
    pass

class C(A):
    def func1(self):
        return 'i am in class C'

class D(B,C):
    pass
#create object from class D
d1=D()
print(d1.func1())

'''
here above, python have first checked for method in class B as per 
the sequence, but it doesn't have any method, so it searched for
that method in class C'''


#4. when both classes don't have that method

print('\n')
print("both classes don't have methods")
class A:
    def func1(self):
        return 'i am in class A'

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass
#create object from class D
d1=D()
print(d1.func1())

'''
when both class, class B and C don't have methods, then python goes
to grandparent class to search, hence here o/p is 'i am in class A'
'''

#5. when method is not present in any of the class
'''
print('\n')
print("method not available with any class")
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass
#create object from class D
d1=D()
print(d1.func1())


here above, no class has method func1, hence it will now search object
class which is superclass of any class, but it doesn't find that
method in super class/object class, hence will throw an error
'''



#******************************
#Method Resolution Order (MRO):
#******************************


'''
In Python, every class whether built-in or user-defined is derived from the object class.
Hence, object class is the base class for all the other classes.

In the case of multiple inheritance a given attribute is first searched in the current class
if it’s not found then it’s searched in the parent classes
The parent classes are searched in a depth-first, left-right fashion and each class is 
searched once.

if again attribute/method is not found in parent class also then it will search in
one level top class(grand parent) and so on, if though not found then it search in
object class.

The order in which searching takes place, is known as a linearization of the class Derived.
and this rule is called as Method Resolution Order (MRO).

'''