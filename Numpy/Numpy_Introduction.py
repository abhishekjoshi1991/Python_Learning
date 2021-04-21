# Numpy Introduction

'''
NumPy is a Python library used for working with arrays.
NumPy stands for Numerical Python.

NumPy arrays are stored at one continuous place in memory unlike lists,
so processes can access and manipulate them very efficiently.

The version string is stored under __version__ attribute.
'''
import numpy as np
print(np.__version__)


'''
The array object in NumPy is called ndarray.
We can create a NumPy ndarray object by using the array() function.
'''
print('\n')
arr = np.array([1,2,3,4,5])

print(arr)
print(type(arr))


#To create an ndarray, we can pass a list, tuple or any array-like object into the array() method,
print('\n')
arr2 = np.array(np.arange(10))
arr3 = np.array((10,20,30))
print(arr2)
print(arr3)


#Dimensions in Array
#1. 0-D Array: have single element or scaler in it
print('\n')
print('dimesions in array')
a = np.array(45)
print(a)
print(a.ndim)

#2. 1-D Array: have 0-D arrays as its elements
print('\n')
b = np.array([1,2,3,4,5])
print(b)
print(b.ndim)

#3. 2-D Array: have 1-D arrays as its elements
print('\n')
c = np.array([[1,2,3],[4,5,6]]) #or (([1,2,3],[4,5,6]))
c1 = np.array([[1,2,3,4]])
print(c)
print(c1)
print(c.ndim)
print(c1.ndim)

#3. 3-D Array: have 2-D arrays as its elements
print('\n')
d = np.array([[[1,2,3],[4,5,6]],[[10,20,30],[40,50,60]]]) #or (([1,2,3],[4,5,6]))
print(d)
print(d.ndim)


'''
An array can have any number of dimensions.

When the array is created, we can define the number of dimensions by using the ndmin argument.
'''
print('\n')
d = np.array([1,2,3,4], ndmin=4)
print(d)