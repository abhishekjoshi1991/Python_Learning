#Function_Recursion


def f1():
    print('in f1')

def f2():
    f1()
    print('in f2')

print(f2())


'''
in above from, we have called function f1 inside function f2,
so while giving the result it has given, in f1 and in f2 both

similar way, we can call the same function inside that function itself,
means calling function f2 within f2, this is called as recursion

In simple words, it is a process in which a function calls itself 
'''

#factorial program using recursion

print('\n')
def fact(num):
    if num<=1:#this condition is must, otherwise infinte recursion will happen
        return 1
    else:
        return num*fact(num-1)
print(fact(5))

'''
working logic of above program:
fact(5)
5*fact(4)
5*4*fact(3)
5*4*3*fact(2)
5*4*3*2*fact(1)
5*4*3*2*1--as fact(1) will return 1, no further iteration will happen as one
return statement is hit, it will get concrete value
'''


#Program to sum of all numbers in nested list

def mysum(a):
	total=0
	for i in a:
		if type(i)==list:
			total=total+mysum(i)
		else:
			total=total+i
	return total
l=[1,2,[10,20,[10,20,10,[10]]],[[10,10],10,[10,20,30]]]
print(mysum(l))
