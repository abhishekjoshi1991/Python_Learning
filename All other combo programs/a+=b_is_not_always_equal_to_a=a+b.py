# a+=b is not always equal to a=a+b


#a+=b always update the value of orginal variable

l1=[1,2,3,4,5]
l2=l1
l1+=[10,20,30]
print(l1)
print(l2)#l2 is also updated

#=====================================================

l3=[1,2,3,4,5]
l4=l3
l3=l3+[10,20,30]#only l3 is changed now but not l4, this creates new list l3 and
#starts referncing to new value, but l4 not changed, it points to old value
print(l3)
print(l4)

