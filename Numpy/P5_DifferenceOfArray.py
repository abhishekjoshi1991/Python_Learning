import numpy as np

'''
numpy.setdiff1d --> Find the set difference of two arrays.
    
Return the unique values in `ar1` that are not in `ar2`
'''
array1 = np.array([0, 10, 20, 40, 60, 80])
print("Array1: ",array1)

array2 = [10, 30, 40, 50, 70]
print("Array2: ",array2)

print("Unique values in array1 that are not in array2:")
print(np.setdiff1d(array1, array2))