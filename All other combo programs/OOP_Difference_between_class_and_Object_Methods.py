#OOP_Difference between class methods and object methods:
#========================================================

#Let's take an example


class Emp:
	nation='india'
	count=0
	def __init__(self,name,salary=20000):
		self.name=name
		self.salary=salary
		Emp.count+=1
	def displayemp(self):
		print('name:',self.name)
		print('salary:',self.salary)
	def empcount(self):
		print('total emp:',self.count)
		print('nation:',self.nation)
'''
(Note*: at a time of object creation if do not pass salary value
then by default salary will be taken as 20000)

be already known, that nation and count are the class variables and
name, salary are the object variables

Object Methods: method in which we use object variables are called
as object methods e.g here is displayemp() method

class methods:method in which we use class variables are called
as class methods e.g here is empcount() method

now as per the python rule, while calling the methods, we must need
to call it using objects only, we can call them directly or using
class means

we can say
e1=Emp('abhi')#this object is created first then

to call say displayemp() method, we need to call it with
e1.displayemp() only, we can not call it as
displayemp() or Emp.displayemp(). because Emp does not go as a
self parameter inside the displayemp method.


so if we call the method using Emp.displayemp() then it will throw
an error that "displayemp() missing 1 required positional argument: 'self'"


Now, if we closly have look on program, then we can see that
for empcount() method (class method) all we are using class
variables like count and nation, then what is use of calling
it with an object

means
'''
e1=Emp('abhishek',50000)
print(e1.empcount())#why we are calling it using object???


'''
but is it not ideal method to call classmethods with objects,
we need to call it with class only, but
we already see above we can not call any method using class or
directly, we always need object

if we call Emp.empcount() then will throw an error

then what is the solution??(python says use decorator)


**decorators**:
#--------------
we have one function to achieve some task for us, and we need to
extend functionallity beyond whatever it does, without affecting
original function behaviour.

decorator name is always started with @, so decorator function
jis bhi function ke sir pe hota hai, uska functionallity extend
hota hai.

below we are using classmethod as a system decorator to use
class for calling the method.

'''

class Emp:
	nation='india'
	count=0
	def __init__(self,name,salary=20000):
		self.name=name
		self.salary=salary
		Emp.count+=1
	def displayemp(self):
		print('name:',self.name)
		print('salary:',self.salary)
	@classmethod
	def empcount(self):
		print('total emp:',self.count)
		print('nation:',self.nation)


#now if we print Emp.enpcount(), it will work

print('\n')
print('using decorator, calling method using class')
e1=Emp('s',25665)
e2=Emp('ad')
print(Emp.empcount())










