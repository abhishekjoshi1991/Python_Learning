# Decoration for function that are taking arguments in its definition

'''
here we will decorate div function, so as to avoid exception of division by zero
'''

def smart_divide(fun):
    def inner(a,b): #we need to pass same no of arguments as in func to be decorated
        print('i am going to divide',a,'by',b)
        if b == 0:
            return 'Cannot divide by zero'
        return fun(a,b)
    return inner

@smart_divide
def div(a,b):
    return a/b

if __name__ == '__main__':
    print(div(10,5))
    print('*'*30)
    print(div(10,0))
