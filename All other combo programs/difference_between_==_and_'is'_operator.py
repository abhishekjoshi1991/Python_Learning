#difference between == and is operator

'''
The == operator compares the values of both the operands and
checks for value equality.
Whereas 'is' operator checks whether both the operands refer
to the same object (memory location)or not.
'''

list1 = [] 
list2 = [] 
list3=list1 

print(id(list1))
print(id(list2))

print(list1 == list2)
   
print(list1 is list2) 

print(id(list3))
print(list1 is list3)

list3=list3+list2#it creates new list3
print(id(list3))
print(list1 is list3) 
   
