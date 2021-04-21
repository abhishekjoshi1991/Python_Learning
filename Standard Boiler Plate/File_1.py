#Standard Boiler Plate File 1

def sum1(a,b):
    return a+b

def dif(a,b):
    return a-b

def mult(a,b):
    return a*b

def divi(a,b):
    return a/b
l1=[1,2,3,4]

print('i am from file 1 outside boiler plate')
print(__name__)#it must print main as a name if we run this file directly

if __name__=='__main__':
    print(mult(10,9))
    print('i am inside boiler plate of file 1')
    print(sum1(10,20))
