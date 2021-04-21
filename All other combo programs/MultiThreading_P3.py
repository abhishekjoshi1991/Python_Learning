
#*******************************************************************************
#Program-3
import threading
print('\n')
print('program to check the how threading takes place')

def run():
    for i in range(50):
        print('Hello')


def run2():
    for i in range(50):
        print('Hi')

t1 = threading.Thread(target=run)  # assigning target to start the thread
t2 = threading.Thread(target=run2)
t1.start()  # starting the execution
t2.start()

'''now from o/p of above program it is clear that two threads t1 and t2 are running 
parallelly now, to print o/p like hello hi, hello hi, hello hi .... we need to 
increase the gap between two execution using time module's sleep method

see MultiThreading_P4

'''