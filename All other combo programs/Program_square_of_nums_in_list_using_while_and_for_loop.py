#Program for Square of Numbers in list
#using while loop
l1=[1,2,3,4,5,6,7,8,9,10,20]
i=0
while i<len(l1):
    print('square is:',l1[i]**2)
    i+=1
else:
    print('success')


#using for loop
for i in l1:
    print('square is:',i**2)
