#*******************************************************************************
#Program-8

print('multithreading using class to call start method')

#here we don't inherit the thread class

import threading as T

class Mythread:
    def f(self):
        for i in range(5):
            print('Hello')

class Otherthread:
    def f(self):
        for i in range(5):
            print('Hi')

#let's create instance of Mythread
m1=Mythread()

#let's create instance of Otherthread
o1=Otherthread()

m1.start()  # starting the execution
o1.start()

'''
here we are calling the start method using class object, but this class
don't have run method to execute, so start won't work here.
 
 in previous programs we are creating object from thread class, that's why 
 after calling start, inbuilt run method from thread class was getting called
 
 
 but for user defined class we don't have run method, so this program 
 throwing an error that 
 'Mythread' object has no attribute 'start'
 
 
 so to avoid this error we must use run method instead of f1 and f2, so our
 run method will overwrite thread class's run method
 
 see program MultiThreading_P9
 '''

