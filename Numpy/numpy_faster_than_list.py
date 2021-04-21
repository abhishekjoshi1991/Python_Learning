import numpy as np
import time
target = 10000000

# adding individual elements of two lists

l1 = range(target)
l2 = range(target)

start = time.time()
result = [(x+y) for x,y in zip(l1,l2)]
end = time.time()

print('time taken by lists:',(end-start)*1000) #multiplied by 1000 to convert to milliseconds

#adding elements from numpy arrays

a1 = np.arange(target)
a2 = np.arange(target)
start = time.time()
result1 = a1+a2 #can do direct addition as in matrices
end = time.time()

print('time taken by np arrays:',(end-start)*1000)



