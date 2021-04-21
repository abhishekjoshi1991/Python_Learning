'''
we can apply same decorator function on multiple other functions those are need
to be decorated.

for e.g. we are having function which calculates a/b/c and other calculates a/b
then, if b=0 or c=0 then it will raise the error and for other function if b=0
then it will raise the error.

so we need to handle both cases using single decorator
'''
def dec(func):
    def inner(*args): #we know when func takes arguments we need to pass to inner
        list1 = []
        list1 = args[1:]  # as we interested in b,c only
        for i in list1:
            if i==0:
                return 'give proper input'
            return func(*args)
    return inner

@dec
def div1(a,b):
    return a/b

@dec
def div2(a,b,c):
    return a/b/c

print(div1(10,20))
print(div2(10,0,20))