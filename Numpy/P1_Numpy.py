# Program to change the value of inside of array to 0 and border value to 1

'''
1  1  1  1
1  1  1  1
1  1  1  1
1  1  1  1

to

1  1  1  1
1  0  0  1
1  0  0  1
1  1  1  1
'''

import numpy as np
a = np.array(np.ones(49,dtype=int)).reshape(7,7)
print(a)
print('\n')
a[1:-1,1:-1] = 0
print(a)