#removing consecutive duplicates from a list
l1=[1,2,5,6,6,1,1,7,8,8,8,9,9,10]

#Method 1:
pre=None
newlist=[]
for i in l1:
    if i!=pre:
        newlist.append(i)
        pre=i
print(newlist)


#Method 2:
print('\n')
print('using groupby from itertools')
from itertools import groupby
new=[i[0] for i in groupby(l1)]
print(new)
'''
see what group by gives as below

for i in groupby(l1):
    print(i)
'''
