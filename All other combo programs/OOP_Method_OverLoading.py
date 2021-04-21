#OOP_Method_Overloading:
#***********************

def func1(a):
    return 'Hello1'

def func1(a,b):
    return 'Hello2'

def func1(a,b,c):
    return 'Hello3'

print(func1(10))
print(func1(10,20))
print(func1(10,20,30))


'''
consider the program, in which we have written functions
with same name, with different structures, with different
behaviours in same class(not mentioned here).

now as python is interpreted language, while calling function
func1(10), python will throw an error of arguments not matching
even we already have defined the func1 with single atrribute.

***thus method overloading is not supported in python***

it can be possible with default parameter inside function
definition

now comment out whole above code and run following code
'''
class Student:
    def hello(self,name='abhi',roll=111):#func with default args
        self.roll=roll
        self.name=name
        print('Name:', self.name,'and','roll:',self.roll)

s1=Student()
print(s1.hello())
print(s1.hello('sukanya'))
print(s1.hello('amit',200))


'''
so with default arguments, method overloading is possible.

so we can not have same method name inside a same class,

'''






        
