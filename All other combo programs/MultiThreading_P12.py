#*******************************************************************************
#Program-11

print('Time taken by program without multithreading')

import threading
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
t1=threading.Thread(target=doubles,args=(numbers,))#as an argument we can pass list ot tuple
t2=threading.Thread(target=squares,args=(numbers,))
begin_time=time.time() #this prints current time
t1.start()
t2.start()
t1.join()
t2.join()
end_time=time.time()
print('total time taken by program:',end_time-begin_time)