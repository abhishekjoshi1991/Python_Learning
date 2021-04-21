#Array Concatenation

#1. using concatenate() function
'''
default axis is zero if not provided
'''

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)
#we cannot concatenate 1D array with axis 1


#Join two 2-D arrays along rows (axis=1)
print('\n')
ar1 = np.array([[1, 2], [3, 4]])
ar2 = np.array([[5, 6], [7, 8]])
ar = np.concatenate((ar1, ar2), axis=1)
print(ar)

#=========================================================================
#2. using stack
#we can concatenate 1D array using stack along any axis
print('\n')
x1 = np.array([1, 2, 3])
x2 = np.array([4, 5, 6])
a = np.stack((x1, x2),axis=0)
print(a)

print('\n')
x3 = np.array([1, 2, 3])
x4 = np.array([4, 5, 6])
b = np.stack((x3, x4),axis=1)
print(b)

'''
horizontal and vertical stack is already defined in numpy_operation.py
let's see dstack method below
'''
print('\n')
x5 = np.array([1, 2, 3])
x6 = np.array([4, 5, 6])
c = np.dstack((x5, x6))
print(c)