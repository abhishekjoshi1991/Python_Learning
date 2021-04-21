import numpy as np
array1 = np.array([0,7, 10, 20, 40, 60])
print("Array1: ",array1)

array2 = [10, 30, 40]
print("Array2: ",array2)

array3=np.arange(9).reshape(3,3)
print(array3)

print("Common values between two arrays:")
print(np.intersect1d(array1, array2))
print(np.intersect1d(array1, array3))