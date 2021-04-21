#difference between while and for loop with example

#suppose i want to change list l1 from [1,2,3,4] to sqaures of
#this numbers [1,4,9,16]

#this can be achieved using while loop but not using for loop

#using while loop
l1=[1,2,3,4]
i=0
while i<len(l1):
    l1[i]=l1[i]**2
    i+=1
else:
    print(l1)

#using for loop
print('\n')
l1=[1,2,3,4]
for i in l1:
    i=i**2
else:
    print(l1)

'''using for loop we are not reaching to elements of list directly,
rather we are calling them for use, so we can not change the elements
'''
    
