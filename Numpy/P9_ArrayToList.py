import numpy as np

x = np.array([[1, 2], [3, 4]])
print('Converted Array:',x)
a2 = x.tolist()
print('Converted List:',a2)
print(type(x))
print(type(a2))