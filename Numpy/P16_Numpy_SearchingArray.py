# Searching Numpy array
'''
we can search the array for certain value and return the indexes where we get match
To search an array, use the where() method.
'''

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)

#The example above will return a tuple: (array([3, 5, 6],)
#Which means that the value 4 is present at index 3, 5, and 6.



#Find the indexes where the values are even:
print('\n')
ar = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(ar%2 == 0)
print(x)


#Search Sorted
'''
There is a method called searchsorted() which performs a binary search in the array, 
and returns the index where the specified value would be inserted to maintain the search order.

The method starts the search from the left and returns the first index where the number 
is no longer larger than the next value.
'''
print('\n')
an = np.array([6, 5, 8, 9, 6])
x = np.searchsorted(an, 7)
print(x)
#the number 7 should be inserted on index 2 to remain the sort order., so that value after
#7 should not be greater than it

print('\n')
ap = np.array([6, 6, 4, 3, 2])
x = np.searchsorted(ap, 5)
print(x) #here value inserted after index 5

'''
default the left most index is returned, but we can give side='right' to return the right most index instead.
'''
