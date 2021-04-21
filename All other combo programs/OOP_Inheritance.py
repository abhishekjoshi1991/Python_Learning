#OOP_Inheritance:
#----------------

'''
In inheritance, a class (usually called superclass)
is inherited by another class (usually called subclass).

subclass inherits all the properties of parent or super class.

subclass generally includes attributes that can not be add into
superclass, otherwise superclass need to get change.

e.g. airbag attribute is added to subclass rather than including it
to superclass. while manufacturing the car, all other attributes
are inherited from parent class like engine,wheels etc.


there are mainly three types of inheritance:
1.single level inheritance
2.multilevel inheritance
3.multiple inheritance

'''

#1. single level inheritance
#--------------------------------------------------------------------
'''
only till one level, another class is inheriting the property.
that means one superclass and one subclass
'''
print('\n')
print('single level inheritance')
class A:#super class
    def feature1(self):
        print('feature 1 is working')

#now let's inherit attributes from class A into class B.

class B(A):#B is inheriting from A, syntax: subclass(superclass)
    def feature2(self):
        print('feature 2 is working')

#let's create object from class B
b1=B()
print(b1.feature1())#b1 will automatically have now attribute feature1
print(b1.feature2())



#2. multi level inheritance
#--------------------------------------------------------------------
'''
more than one level, another class is inheriting the property.
that means one superclass and many subclass
'''

print('\n')
print('multi level inheritance')
class A:#super class
    def feature1(self):
        print('feature 1 is working')

#now let's inherit attributes from class A into class B.

class B(A):#B is inheriting from A, syntax: subclass(superclass)
    def feature2(self):
        print('feature 2 is working')

#now let's inherit attributes from class A into class C also.

class C(A):#B is inheriting from A, syntax: subclass(superclass)
    def feature3(self):
        print('feature 3 is working')

#let's create object from class B and C
b1=B()
c1=C()
print(b1.feature1())
print(b1.feature2())
print(c1.feature1())
print(c1.feature3())

#-------------------------------------------------------------------
'''
let's create employee as super class/ parent class and programmer and
manager as sub class/child class/derived class.

first we will create employee class in another file with name
employee_inherit_main.py, and then we will import that file here.
'''

print('\n')
print('employee and programmer example')
from employee_inherit_main import Employee
class Programmer(Employee):
    def __init__(self,name,salary,project):
        Employee.__init__(self,name,salary)#or super(Programmer,self).__init__(name,salary)
        self.project=project
    def display_employee(self):
        Employee.display_emp(self)#or super(Programmer,self).display_emp()
        print('Project:',self.project)

class Manager(Employee):
    pass

p1=Programmer('abhi',25000,'PHP')
print(p1.display_employee())

'''
here above,
Employee.__init__(self,name,salary) means for construction purpose,
send name and salary to employee class __init__. wahase woh construct
hogar yaha aayega


there are two ways by which we can call parameter from parent class:

1. Employee.__init__(self,name,salary) 
2. super(Programmer,self).__init__(name,salary)#no self inside init
similaraly

Employee.display_emp(self) or super(Programmer,self).display_emp()

so super of programmer is Employee

'''
#*************************************
# now create object from Manager class
print('\n')
print('o\p from manager class')
m1=Manager('Sukanya')
print(m1.display_emp())
print(m1.emp_count())#or print(Manager.emp_count())

'''when we start the construction of m1 object, then it will go to
init method of Manager, but here manager class don't have init
method, so python will check for init method at one level up that is
in parent class, now parent class have init, so at that name=sukanya
and default salary of 20000 will be passed.

so always remember, if object does not find init method or other method,
control always goes to parent class to check for init method or that method
(like emp_count or display_emp)

'''


#****************************************************************************
#****************************************************************************

'''
when class is does not inheriting other class, then by default it inherits
object class of system,
thus generally hidden syntax of class is:

class Employee(object):
'''
#****************************************************************************
#****************************************************************************




