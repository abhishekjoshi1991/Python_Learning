#Program to create dictionary using two list with condition
'''
condition 1:
if length of two list is different then it must print different lengths

condition 2:
if list have duplicate elements then it must print duplicated keys

else it must create dictionary using two lists

'''

def dict(l1,l2):
    if len(l1)!=len(l2):
        return 'different lengths'
    elif len(l1)!=len(set(l1)):
        return 'duplicated elements'
    else:
        d={}
        for i in range(len(l1)):
            d[l1[i]]=l2[i]

    return d

print(dict([1,2,3,4,5],[10,20,30,40]))
print(dict([1,2,3,2],[10,20,30,40]))
print(dict([1,2,3,4],[10,20,30,40]))


'''we can not use
for i in l1:
    for j in l2:
        d[i]=j
this will give wrong result
'''

#=========================================================================

#using zip operator
print('\n')
print('o\p using zip')
def func(a,b):
    if len(a)!=len(b):
        return 'different lengths'
    elif len(a)!=len(set(a)):
        return 'duplicated elements'
    else:
        return dict(zip(a,b))

print(func([1,2],[10,20]))
