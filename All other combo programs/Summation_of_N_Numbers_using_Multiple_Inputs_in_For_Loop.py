#summation of N numbers using input statement inside for loop

N=int(input('enter no of value for which addition to be done:'))
list2=[]
for i in range(N):
	n=int(input('enter each value seperately:'))
	list2.append(n)

print(list2)
addition=0
for each in list2:
    addition+=each

print(addition)


#using list comprehension

list2=[int(input('enter each value seperately:')) for i in range(N)]
print(sum(list2))
