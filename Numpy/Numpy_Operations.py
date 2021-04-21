#Numpy_Operations_On_Array
import numpy as np

#1. to find dimensions of an array
#already discussed in Introduction part

a1 = np.array([1,2,3,4,5])
print(a1.ndim)
#===================================================================================

#2. to get the item size
print('\n')
print(a1.itemsize) #so each element takes 4 bytes
#===================================================================================

#3. to know the data type stored in the array
print('\n')
print(a1.dtype)
#===================================================================================

#4. to know the size of array (no of elements in it)
print('\n')
print(a1.size)
a2 = np.array([(1,2,3,4),(5,6,7,8)])
print(a2.size)
#===================================================================================

# 5. to get shape of array (i.e. dimensions in form m*n)
print('\n')
a4 = np.array(((2,3,4),(5,6,7)))
print(a4.shape) #two rows and three columns
a5 = np.array([1,2,3,4,5,6,7])
print(a5.shape) #7 columns and zero rows ans structure of o/p is 7,
d = np.array([[[1,2,3],[4,5,6]],[[10,20,30],[40,50,60]]])
print(d.shape)
#===================================================================================

# 6. Reshape the array (changing the rows and column)
ar = np.array(np.arange(16))
ar = ar.reshape(4,4) #we need to over write to variable
print(ar)
ar1 = np.array(np.arange(16))
ar1 = ar1.reshape(8,2)
print(ar1)
#===================================================================================

# 7. Indexing of array
print('\n')
x = np.array([0,15,2,3,4])
print(x[1])
# indexing 2D Array, access second element from second dim
x1 = np.array([[10,20,30],[40,50,60]])
print(x1[1,1])
'''
[10,20,30] is zero dimension and [40,50,60] is 1st dimension, and in x1[1,1] 
first letter is for dim and second letter is for index position
so index 1st index from 1st dimension
'''
# indexing 3D Array, Access the third element of the second array of the first array
arrr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arrr[0, 1, 2])
'''
The first number represents the first dimension, which contains two arrays:
[[1, 2, 3], [4, 5, 6]] and [[7, 8, 9], [10, 11, 12]]

Since we selected 0, we are left with the first array:
[[1, 2, 3], [4, 5, 6]]

The second number represents the second dimension, which also contains two arrays:
[1, 2, 3] and [4, 5, 6]
Since we selected 1, we are left with the second array:
[4, 5, 6]
'''
#Negative indexing, Last element from 2nd dim
p = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(p[-1,-1]) #or p[1,-1]

#to grab all last elements from dims, this is actually a slicing
p1 = np.array([[1,2,3,4,5], [6,7,8,9,10],[11,12,13,14,15]])
#here we need to grab element 5 and 10
#so we can do that as
print(p1[0:,4]) # 0: give all the rows from 0 and in that all last elements at index 4
#===================================================================================

# 8. Slicing of array
'''
slicing means taking elements from one given index to another given index
p[a:b]--> including a and excluding b
'''
print('\n')
#slicing 1D array
x = np.array([58,69,68,61,23])
print(x[1:3])
#negative slicing
print(x[-3:-1])
#slicing 2D array, From the second element, slice elements from index 1 to index 4
y = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(y[1,1:4])
#slicing 2D array, From both elements, return index 2
print(y[0:,2])

#===================================================================================

# 9. linspace
#used to create no of elements as specified between start to end, equispaced
#create 5 elements between 1 to 4, including 1 and 4
print('\n')
ax = np.linspace(1,4,5)
print(ax)

#===================================================================================

# 10. min, max and sum of elements from array
print('\n')
az = np.array([[1,2,3,4,5],[10,20,30,40,50]])
print(az.min())
print(az.max())
print(az.sum())

#===================================================================================

# 11. axis concept
'''
axis 0 --> is for y axis i.e. for columns or IS THE DIRECTION ALONG THE ROWS |v
axis 1 --> is for x axis i.e for rows or IS THE DIRECTION ALONG THE COLUMNS --->
'''
print('\n')
print('axis concept')
al = np.array([[1,2,3,4,5],[10,20,30,40,50]])
print(al.sum(axis=0)) #gives column wise addition
print(al.sum(axis=1)) #gives row wise addition

#===================================================================================

# 12. sqrt and std deviation
a = np.array([[1,2,3,4,5],[100,144,30,40,50]])
print(np.sqrt(a)) #sqrt and std is available with np not with a(variable)
print(np.std(a))

#===================================================================================

# 13. addition, mult, div, sub of array element wise
print('\n')
b1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
b2 = np.array([[9,7,8],[6,5,4],[3,2,1]])
print(b1+b2)
print(b1-b2)
print(b1*b2)
print(b1/b2)

#===================================================================================

# 14. Concatenating array (vertical and horizontal stacking), ravel function
print('\n')
b1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
b2 = np.array([[9,7,8],[6,5,4],[3,2,1]])
print(np.vstack((b1,b2))) #need to provide tuple of array
print(np.hstack((b1,b2)))

#to convert elements into single row
print(np.ravel(b1))

#===================================================================================

# 15. slice referencing
#used to change the value in array with the help of slicing
print('\n')
a = np.array(np.arange(16)).reshape(4,4)
print(a)
#now let's change the value of last two column to 99
a[:,2:]=99
print(a)

#===================================================================================

# 16. greater than, less than operations
print('\n')
a= np.array(np.arange(16)).reshape(4,4)
print(a)
print(a>10)
#it runs condition on each element and returns true or false

#to filter all the elements based on True only we can use
print(a[a>10])
#so this only collects the elements for which condition is True and convert them to 1D array

#similaraly to filter the elements that are divisible by 2 only
print(a[a%2==0])

#===================================================================================

# 17. Flaten function: to convert multi dim to 1D
print('\n')
a= np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a.flatten())

#===================================================================================
# 18. Transpose

print('\n')
a= np.array([[1,2,3],[4,5,6],[7,8,9]])
print('before transpose:',a)
a= a.transpose()   #or a.T
print('After transpose:',a)

#===================================================================================
# 19. flat, throws iterator, when use for loop gives all elements

#===================================================================================
# 20. argmax() and argmin() methods
'''
Gives index position where max and min value is present
'''
print('\n')
a= np.array([[1,2,3],[4,5,6],[7,1,0]])
print('argmax and argmin')
print(a.argmax()) #gives the o/p after flattening the array
print(a.argmin()) #gives the o/p after flattening the array
#with axis attribites
print(a.argmin(axis=0)) #compare 1,4,7 then 2,5,1 and 3,6,0
print(a.argmin(axis=1))

#===================================================================================
# 20. argsort() methods
'''
sorts the index position according to element values
'''
print('\n')
a= np.array([1,50,25,7,9])
print('argsort')
print(a.argsort())
# we can also use here with axis for 2D array



#to check which are methods and which are attributes for numpy visit:
#https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html

