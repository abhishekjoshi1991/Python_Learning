#*******************************************************************************
#Program-11

print('Time taken by program without multithreading')

import threading as T
import time


def doubles(numlist):
    for i in numlist:
        print('doubles:',i*2)
        time.sleep(1)

def squares(numlist):
    for i in numlist:
        print('squares:',i**2)
        time.sleep(1)

numbers=[1,2,3,4,5]
begin_time=time.time() #this prints current time
doubles(numbers)
squares(numbers)
end_time=time.time()
print('total time taken by program:',end_time-begin_time)