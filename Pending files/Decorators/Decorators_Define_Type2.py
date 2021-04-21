'''
We can use the @ symbol along with the name of the decorator function and
place it above the definition of the function to be decorated.
'''

def make_pretty(func):
    def inner():
        print('i am decorated')
        func()
    return inner

@make_pretty
def extraordinary():
    print('i am extra-ordinary')

extraordinary()


'''
so

@make_pretty
def extraordinary():
    print("I am extraordinary")
    
is equivalent to

def extraordinary():
    print("I am extraordinary")
extraordinary = make_pretty(extraordinary)
'''