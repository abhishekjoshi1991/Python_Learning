import numpy as np
import sys

l1 = range(100)
l2 = range(100)

a1 = np.arange(100)
a2 = np.arange(100)

print(sys.getsizeof(0)*len(l1)) #size of any object say 0 * no of elements in list
print(sys.getsizeof(0)*len(l2))


print(a1.size*a1.itemsize) #a1.size == no of elements in array * a1.itemsize is space taken by one element ==4bytes
print(a2.size*a2.itemsize)

