#Multithreading:
#***************

'''
multithreading is a way of achieving multitasking (simultaneous process executed
at a same time). In multithreading, the concept of threads is used.

A thread is a sequence of such instructions within a program that can be executed
independently of other code. in simple word  thread is a subset of a any process!


Multithreading is defined as the ability of a processor to execute multiple threads
concurrently.

In a simple, single-core CPU, it is achieved using frequent switching between
threads. This is termed as context switching. In context switching,
the state of a thread is saved and state of another thread is loaded


consider the program 1 below, without incorporating concept of multithreading in
it.

when we execute two classes, first function 1  inside class hello is executed
wholly then only second function from class Hi is executed.

'''

#Program-1

print('simple program without multithreading')

class Hello:
    def run(self):
        for i in range(5):
            print('Hello')


class Hi:
    def run(self):
        for i in range(5):
            print('Hi')

t1=Hello()
t2=Hi()
t1.run()
t2.run()

'''
from above we will see that firstly five times hello is printed and once printing
is complete then only five times Hi will be printed.

so this is not case of multithreading

now we want to print Hello then Hi then Hello then Hi, or Hello Hi in some
combination parallelly, then we can use concept of multithreading.

for multithreading we must have independent task, if dependency is their then
it will create a problem

for multithreading we need to import threading library first
'''







