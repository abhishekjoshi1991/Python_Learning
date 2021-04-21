#*******************************************************************************
#Program-6

import threading,time
print('\n')
print('program to check the how threading takes place using time gap and print statement at last')

def run():
    for i in range(5):
        print('Hello')
        time.sleep(1) #after each execution stop for 2 sec


def run2():
    for i in range(5):
        print('Hi')
        time.sleep(1)  # after each execution stop for 2 sec

t1 = threading.Thread(target=run)  # assigning target to start the thread
t2 = threading.Thread(target=run2)
t1.start()  # starting the execution
time.sleep(0.2)
t2.start()

print('hello world')

'''
from o/p it is clear that, last print statement may get executed anywhere in between t1 and t2
this is because print('hello world') is executed by main thread. so after first iteration of 
t1 and t2, main thread prints last statement.

so we need to stop execution of main thread, unless execution of t1 and t2 get complete

so to print this statement only at last, we need to specify join method,
join method forces main thread to stop execution till t1 an t2 thread complete their
 execution
 
 see MultiThreading_P7'''