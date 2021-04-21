# Difference between copy and view
'''
The main difference between a copy and a view of an array is that the copy is a new array,
and the view is just a view of the original array.

The copy owns the data and any changes made to the copy will not affect original array,
and any changes made to the original array will not affect the copy.

The view does not own the data and any changes made to the view will affect the original array,
and any changes made to the original array will affect the view.
'''

import numpy as np

# Program -1:
#  Make a copy array, change the original array, and display both arrays

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 50 #changes to original array

print(arr) #only changes to original array
print(x) #no changes to copied array

#=================================================================================================
# Program -2:
#  Make a copy array, change the copied array, and display both arrays
print('\n')
arr1 = np.array([1, 2, 3, 4, 5])
x = arr1.copy()
x[0] = 50 #changes to copied array

print(arr1) #no changes to original array
print(x) #changes to copied array

#=================================================================================================
# Program -3:
# Make a view of an array, change the original array, and display both arrays:
print('\n')
arr2 = np.array([1, 2, 3, 4, 5])
x = arr2.view()
arr2[0] = 50 #changes to original array

print(arr2) #changes to original array
print(x) #viewed array is also changed

#=================================================================================================
# Program -4:
# Make a view of an array, change the viewed array, and display both arrays:
print('\n')
arr3 = np.array([1, 2, 3, 4, 5])
x = arr3.view()
x[0] = 20 #changes to viewed array

print(arr3) #changes to original array also
print(x) #viewed array is changed

#=================================================================================================
# Program -5:
# to check  if Array Owns it's Data
'''
copies owns the data, and views does not own the data

NumPy array has the attribute base that returns None if the array owns the data.
'''

print('\n')
ar = np.array([1, 2, 3, 4, 5, 6, 7])

x = ar.copy()
y = ar.view()

print(x.base) #None represents the array owns the data
print(y.base)