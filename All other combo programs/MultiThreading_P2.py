# *******************************************************************************
# Program-2

print('\n')
print('simple program with multithreading to print thread name and process id')

'''
even if we are not calling multithreading, program is running under single thread
called as main thread, so every program is run by a main thread
'''
import threading, os


def run():
    print('thread name:', threading.current_thread().name)  # to print thread name
    print('Process id of this thread is {}'.format(os.getpid()))
    for i in range(5):
        print('Hello')


def run2():
    print('thread name:', threading.current_thread().name)
    print('Process id of this thread is {}'.format(os.getpid()))
    for i in range(5):
        print('Hi')


print('thread name:', threading.current_thread().name)  # this comes under main program so it is main thread
print('Process id of this thread is {}'.format(os.getpid()))
t1 = threading.Thread(target=run)  # assigning target to start the thread or creating thread class ka object
t2 = threading.Thread(target=run2)
t1.start()  # starting the execution, by calling start we actually start exceution of run method
t2.start()

'''from above it is clear that, all process id is same only thread is different
i.e single process is getting run by multi threads

as we are taking less iterations, we feel like that after finishing t1, t2 is
started, but if take more iterations then it will not be this case
see MultiThreading_P3 now'''


#IMPORTANT::::

#when we say t1.start() then internally it will call run method from threading class


'''
here we have started the thread using thread object t1 and t2
but while defining the own class we don't have run method inside it
so we need to define run method explicitly inside class so that
we can call that method using object/instance of our class'''

#here we have not defined any class for now but see MultiThreading_P8