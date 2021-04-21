#Object Oriented Programming:
#============================

'''
OOP: it is programming method which uses concept of both data(student
details in google form)and object.

Just like we call everything we see in real-life as objects,
we call every entity in OOP as objects.

Let take example of car  class:

Car
--Attributes/parameters--
wheels
engine

__behaviour/methods/functions--
to accelerate
to stop

using above attribute and behaviour, when we make car a physically
those car produced are called as "objects", those possesses all
property of that car class like wheel, engine etc

so car is parent called as class and different car manufactured
are objects.

Another example is of google form, in google form we create attributes
for students details (name,roll, age etc) then student filled their
data in it, so at background one object is created for that specific
student, this object posseses all attributes of that student form(class).

so technically class is blueprint(contain all details) and object is
instance of a class.
A class can be defined as an object’s blueprint, description, or
definition. We can use the same class as a blueprint for creating
multiple different objects.


Let's create first class:
'''

class Student:#(convention is to use cap letter at start of class name)
    def __init__(self,roll,name):
        self.roll=roll
        self.name=name
    def display(self):
        print('Name:',self.name)
        print('Roll:',self.roll)

s1=Student(100,'abhi')
print(s1.roll)
print(s1.name)
print(s1.display())


'''
let's understand now its working:
1. inside __init__ we pass "self"(any variable) as default argument,
and other arguments like roll and name
2. in methods (special type of function) here display(), we pass
"self" as a argument/parameter, if we don't pass self as a argument
here (but considered as no argument)then will throw an error that
display takes 0 argument but 1 is given when we call this method using
object

3. when we say s1=Student(100,'abhi'),(called as construction of object)
then s1 is called as object we are creating, (100,'abhi') will be
arguments passed for roll and name and Student is act as
constructor for object,

so when we call this statement,(class is called as function Student())
then student class ka init method call hota hai jisme
self ki jagah s1(variable name) jata hai, roll ki jagah 100 and
name ki jagah 'abhi' jata hai, means
__init__(s1,100,'abhi').

so inside __init__ we have written, self.roll=roll, means
it will be treated for this as s1.roll=100 and self.name=name means
s1.name='abhi'

so for last print statement we will get o/p as 100 and 'abhi'


and to call method (here display),
when we say s1.display() then student claas ka display() method call
hota hai jisme s1 will be passed as self argument display(s1).
it is similar to calling methods for strings, list etc. str.split(),
str.join('')

so method must be called with parantheses only.


so in shell window, after construction of object, when we type s1. and
press tab button we will get (roll,name,display) as an options


in this way, we can create multiple objects

like

s2=Student(200,'sukanya') and so on


so when we check dir(s1) we will get display, name, roll as functions
'''

print(dir(s1))

#=======================================================================
#=======================================================================

#Program to Create circle class:
#===============================
print('\n')
print('circle class')
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.142*self.radius*self.radius
    def perimeter(self):
        return 2*3.142*self.radius

c1=Circle(10)
print(c1.area())
print(c1.perimeter())

'''
we can also do like this,
class Circle:
    pi=3.142
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return Circle.pi(or self.pi)*self.radius*self.radius
    def perimeter(self):
        return 2*Circle.pi*self.radius

or
class Circle:
    def __init__(self,radius):#for hardcoded value we don't need to spcify pi
        self.radius=radius
        self.pi=3.142
    def area(self):
        return self.pi*self.radius*self.radius
    def perimeter(self):
        return 2*self.pi*self.radius

'''

#=======================================================================
#=======================================================================

#concept of class variable and object variables:
#===============================================

'''
for differenet object like s1,s2 etc. we have different names, roll etc
these are called as object variables specific to objects

but let's say nation='india' is common for all objects, then we don't
specify it as an argument inside __init__, instead of that we
specify it inside the class before __init__ method

so when we call object.tab then we will get (name,roll,nation,display)
as methods available for that object.

this nation is then called as class variable

let's see how to define it
'''

print('\n')
print('difference between class and object variable')
class Student1:
    nation='india'#class variable
    count=0#class variable
    def __init__(self,roll,name):
        self.roll=roll
        self.name=name
        Student1.count+=1
    def display(self):
        print('Name:',self.name)
        print('Roll:',self.roll)

s1=Student1(100,'abhi')
s2=Student1(200,'sukanya')
print(s1.roll)
print(s1.name)
print(s1.nation)#s1 has read access of nation
print(s1.display())

'''
for count, we increasing count value inside init, but value of
count we be same for both s1 and s2,if we have created only two objects

s1.count and s2.count will have same value as 2

because count ka copy class ke pass hai, jitne objects hum banayenge
count ka value increase hoga, aur wahi value print hogi for all objects


also let's say if we do s1.count=999, then it possible but it is considered as
adding new attribute to s1 having value 999, but s2.count will not be 999, its
value will depend on what value of count is available with class.

we cannot delete s1.count using del(s1.count) as s1 have only read access of s1
'''


'''
we can change attribute's value specific to any object any time
means
'''
print('\n')
print("changed attribute's value")
s1.nation='US'
print(s1.nation)#will changed to US
print(s2.nation)#will be india


'''
to change class variable

after changing class variable to UK, s1 will not have that UK value as
we have already changed it to US, but for s2 it will UK

class variable change karne ka access only class ke pass hai, thats
why we called Student1.nation
'''

print('\n')
print("changed class variable value")
Student1.nation='UK'
print(s1.nation)#will be same as US
print(s2.nation)#will be now UK

'''
to add whole new attribute to object:

we can add whole new attribute to object, even if it is not defined
in class definition, because all these objects functions independently

lets add attribute 'dept' to s1, so only s1 will have that attribute
if we check dir(s1) but s2 won't have that attribute
'''

print('\n')
print("adding whole new attribute to object")
s1.dept='mech'
print(s1.dept)
print(dir(s1))
print(dir(s2))

'''
similarly we can delete specific attribute also from object

del s1.dept
'''

#=======================================================================
#=======================================================================

#defining instance/object variable inside methods
#================================================
print('\n')
print("defining object variable inside the method")
class Stud:
    def __init__(self,roll):
        self.roll=roll
    def setadd(self,address):
        self.address=address#defined variable inside method
    def getadd(self):
        return self.address
s1=Stud(101)#instance/object is created
print(s1.roll)
s1.setadd('ravet')
print(s1.getadd())


#=======================================================================
#=======================================================================

#difference between getattr and setattr
#=====================================

print('\n')
print('difference between getattr and setattr')
class Student1:
    def __init__(self,roll,name):
        self.roll=roll
        self.name=name
    def display(self):
        print('Name:',self.name)
        print('Roll:',self.roll)

s1=Student1(50,'A')
print(s1.roll)
#we can change atrribute value using setattr
setattr(s1,'roll',51)#same as s1.roll=51
print('new roll value')
print(s1.roll)

#to get value of attribute use getattr
print(getattr(s1,'roll'))#attribute must be specified in str format(same as s1.roll)




#=======================================================================
#=======================================================================

#constructiong a class without __init__:
#======================================

'''
we can define the class without use of __init__ method,
'''
print('\n')
print('class without __init__')
class A:
    def feature(self):
        print('feature 1 is working')

a1=A()#creating an object
print(a1.feature())



















