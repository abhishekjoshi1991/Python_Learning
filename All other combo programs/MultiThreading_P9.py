#*******************************************************************************
#Program-9

print('program using overridden run method inside a class')

#here we need to inherit the thread class

import threading as T

class Mythread(T.Thread):
    def run(self):#run method is overridden
        for i in range(5):
            print('Hello')

class Otherthread(T.Thread):
    def run(self):
        for i in range(5):
            print('Hi')

#let's create instance of Mythread
m1=Mythread()

#let's create instance of Otherthread
o1=Otherthread()

m1.start()  # starting the execution
o1.start()