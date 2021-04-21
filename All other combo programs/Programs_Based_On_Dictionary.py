#Programs based on dictionary
#https://www.w3resource.com/python-exercises/dictionary/?passed=passed

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#1. creating structure like {1:'A',2:'B'....26:'Z'}
d={}
for i in range(1,27):
    d[i]=chr(i+64)
print(d)


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#2. generate dictionary in the form (x:x**2)
print('\n')
d={}
for i in range(1,10):
    d[i]=i**2
print(d)


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
