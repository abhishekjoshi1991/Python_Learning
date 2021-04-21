# Iterating over array

# Program-1
# iterating on 1D array

import numpy as np

arr = np.array([1, 2, 3])
for x in arr:
  print(x)

#============================================================================

# Program-2
# iterating on 2D array

print('\n')
ar = np.array([[1, 2, 3], [4, 5, 6]])
for i in ar:
    print(i)
#on iteration, we will get individual dimension as an i, we need to again
#iterate over it to get all elements or to unpack all the elements

for x in ar:
  for y in x:
    print(y)

#============================================================================

# Program-3
# iterating on 3D array
'''
same as that of 2D array, need to iterate thrice to unpack the values
'''
print('\n')
a = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in a:
  for y in x:
    for z in y:
      print(z)

p =np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(p.ndim)

#============================================================================

# Program-4
# Iterating Arrays Using nditer()
'''
In basic for loops, iterating through each scalar of an array we need to use n for loops 
which can be difficult to write for arrays with very high dimensionality.
for e.g we need 3 for loops for 3D array
'''
print('\n')
x = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in np.nditer(x):
  print(x) #using single loop we can unpack the data


#============================================================================

# Program-4
# Iterating Array With Different Data Types
'''
We can use op_dtypes argument and pass it with expected datatype to change the datatype of 
elements while iterating

NumPy does not change the data type of the element in-place , it needs extra space called as buffer
in order to enable it in nditer() we pass flags=['buffered']
'''
print('\n')
ap = np.array([1, 2, 3])

for x in np.nditer(ap, flags=['buffered'], op_dtypes=['S']):
  print(x)




#Iterate through every scalar element of the 2D array skipping 1 element:
print('\n')
m = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(m[:, ::2]):
  print(x)