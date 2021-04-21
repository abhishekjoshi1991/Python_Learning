#multiple input in python

#using .split() method
x,y=input('enter the multiple value space seperated:').split()
print(x)
print(y)


#Note** --> x,y,z=[10,20,30]-->x=10,y=20 etc.

#using list comprehensions
x,y=[int(i) for i in input('enter the multiple value space seperated:').split()]
print(x)
print(y)

