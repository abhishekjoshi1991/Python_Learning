#*******************************************************************************
#Program-7


import threading,time
print('\n')
print('program to check the how threading takes place using join method')

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

t1.join()
t2.join()

print('hello world')