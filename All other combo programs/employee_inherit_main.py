class Employee:
    count=0
    nation='india'
    def __init__(self,name,salary=20000):
        self.name=name
        self.salary=salary
        Employee.count+=1
    def display_emp(self):
        print('name:',self.name)
        print('salary:',self.salary)
    def emp_count(self):
        print('totalEmp:',self.count)
        print('Nation:',self.nation)
