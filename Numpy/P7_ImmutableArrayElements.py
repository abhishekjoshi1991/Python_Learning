import numpy as np
x = np.zeros(10)
x[0] = 156
print(x)

x.flags.writeable = False #by changing this flag to False, we assure immutability
#default flag is True

print("Test the array is read-only or not:")
print("Try to change the value of the first element:")
x[0] = 1