#OOP_DuckTyping (Polymorphism):
#*****************************

'''
let's create one class named laptop in which we will defined one method 'code'.
in that method as an argument let's pass
an object 'ide' (or other name). then we are calling method for that
object say 'execute'.
ide.execute()

it is similar to passing str as a object and calling split method
for that object.
str.split()

now to create object 'ide', we need define a class, say we will create
two classes Pycharm and Mycharm which will be having execute function
written in it. both these classes will have different behaviours

now we don't know type of 'ide' object, whether it is str, int, float??
so we can change type of 'ide' object from Pycharm to Mycharm provided
it carries the method execute with it, this is called as Dynamic Typing.

thus using duck typing we can give new functionality to an object.
'''

#creating class for Laptop, having a method which takes obj as an argument
class Laptop:
    def code(self,ide):
        ide.execute()

#creating first class to create obj 'ide'
class Pycharm:
    def execute(self):
        print('compling')
        print('running')

#creating second class to create obj 'ide'
class Mycharm:
    def execute(self):
        print('compling')
        print('running')
        print('spell check')

#1.
print('\n')
print('o/p after creating ide object from Pycharm')
#let's create obj from laptop class
l1=Laptop()

#create object 'ide' from Pycharm class first
ide=Pycharm()

#calling code method for laptop class object(l1)
print(l1.code(ide))#here will get o/p as compling and running



#2.
print('\n')
print('o/p after creating ide object from Mycharm')
#let's create obj from laptop class
l1=Laptop()

#create object 'ide' from Mycharm class first
ide=Mycharm()

#calling code method for laptop class object(l1)
print(l1.code(ide))#here will get o/p as compling, running and spell check



'''
so in a glance, if class having method execute, then we can create ide object
from them, so o/p of l1.code(ide) will different based on from what class
ide object is coming


so general phrase is,
If thing is looks like a duck and quacks like a duck, then that thing is a duck
'''



print('\n')
print('********************************')
print('duck example')
print('********************************')
class Duck:
    def look(self):
        print('looks like duck')
    def quack(self):
        print('quacks like a duck')

class Fly:
    def look(self):
        print('fly looks like duck')
    def quack(self):
        print('fly quacks like a duck')

class Airplane:
    def method(self,thing):
        thing.look()
        thing.quack()

a1=Airplane()
thing=Duck()#here thing is coming from duck class
print(a1.method(thing))

thing=Fly()#here thing is coming from fly class
print(a1.method(thing))

'''
here behaviour of airplane is different based on from which class
we deriving the object 'thing'
'''