#Program to remove duplicates from list without using set function

a=[1,22,3,6,5,2,3,5,6,22,3,5,1]
b=[]
for i in a:
    if i in b:
        pass
    else:
        b.append(i)
print(b)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#using enumerate function (enumerate gives index numbers and values)
a=[1, 5, 3, 6, 3, 5, 6, 1]

b=[i for n,i in enumerate(a) if i not in a[:n]]
print(b)

'''above will work like this,
for n,i in enumerate(a), will gives n values as 0,1,2,3,4,5,6,7 and i values
will be elements in a.
'''

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#using list comprehensions
a=[1, 5, 3, 6, 3, 5, 6, 1,8]
b=[]
[b.append(i) for i in a if i not in b]
print(b)
