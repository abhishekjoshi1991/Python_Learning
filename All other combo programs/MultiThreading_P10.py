#*******************************************************************************
#Program-10

print('creating thread using thread object without inheriting thread class')

import threading

class Mythread:#we are not inheriting from thread class
    def f1(self):#run method is overridden
        for i in range(5):
            print('Hello')

    def f2(self):
        for i in range(5):
            print('Hi')

#as we are not inheriting from thread class, we need to call start method using thread class object only
#and not from Mythread object

obj=Mythread()
t1=threading.Thread(target=obj.f1)#created thread class obj using target as Mythread objects method
t2=threading.Thread(target=obj.f2)

t1.start()
t2.start()
