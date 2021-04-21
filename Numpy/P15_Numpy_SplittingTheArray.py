# splitting the array

'''
Splitting is reverse operation of Joining.
We use array_split() for splitting arrays, we pass it the array we want to
split and the number of splits.
'''
import numpy as np

#split the array into three parts
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr) #The return value is an array containing three arrays

#If the array has less elements than required, it will adjust from the end accordingly.
print('\n')
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 4)
print(newarr)
print(newarr[0])
print(newarr[1])
print(newarr[2])


#splitting 2D array
print('\n')
arr1 = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr1 = np.array_split(arr1, 3)
print(newarr1) #it returns three 2-D arrays.

#we also have hsplit, vsplit and dsplit method and also split array based on axis
