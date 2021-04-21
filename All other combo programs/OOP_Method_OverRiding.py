#OOP_Method_OverRiding:(it is concept of polymorphism-one function
#can beahve differently)
#**********************

'''
when we have same name of function, with same structure and with different
behaviours,

means in parent class we have some method name with certain
behaviour, in child class we have method with same name, but has
different behaviour then whatever statements we have inside that
method in child class gets executed


consider the example of again of parent class from employee_inherit_main.py
in this class of Employee we have method with name display_emp,

let's use name method here while defining the programmer class
'''
from employee_inherit_main import Employee
class Programmer(Employee):
    def __init__(self,name,salary,project):
        Employee.__init__(self,name,salary)
        self.project=project
    def display_emp(self):
        print('hello')

p2=Programmer('jose',25655,'IT')
print(p2.display_emp())


'''
from output,we see that, display_emp() method priniting 'Hello'
and not priniting data
print('name:',self.name)
print('salary:',self.salary) from parent class.

that means child class has overridden method display_emp and
thus showing 'hello' output
'''
