#Program to reverse a list

a=[1,2,3,4,5]

#using reverse() function
a.reverse()
print(a)

#----------------------------------------------------------
print('\n')
a=[1,2,3,4,5,6]
b=[]
for i in range((len(a)-1),-1,-1):
    b.append(a[i])
print(b)
#----------------------------------------------------------

#reverse using slicing operator
a=['abhi','abc','xyz']
b=a[::-1]
print(b)

