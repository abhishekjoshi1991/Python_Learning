'''
when we need to pass parameter to decorator, then we need to defined additional function
which takes parameter outside the decorator function as below

we need to wrap this decorator

def up(func):
    def inner():
        return func()
    return inner

inside another function
'''

def outer(expression):
    def up(func):
        def inner():
            return func() + expression
        return inner
    return up

@outer(' abhishek')
def ordinary():
    return 'good morning'

print(ordinary())