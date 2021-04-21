#*******************************************************************************
#Program-4
import threading,time
print('\n')
print('program to check the how threading takes place using time gap')

def run():
    for i in range(50):
        print('Hello')
        time.sleep(1) #after each execution stop for 2 sec


def run2():
    for i in range(50):
        print('Hi')
        time.sleep(1)  # after each execution stop for 2 sec

t1 = threading.Thread(target=run)  # assigning target to start the thread
t2 = threading.Thread(target=run2)
t1.start()  # starting the execution
t2.start()

'''
so from above we clear, how we can use sleep function, here again o/p is not
as expected. but idea is clear

this is called as collsion of two threads, so to avoid this collision we
can use another sleep after t1.start

see MultiThreading_P5'''