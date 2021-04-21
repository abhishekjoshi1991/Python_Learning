#here we will use two decorators above function to be decorated

def star(func):
    def inner(*args):
        print('*'*30)
        func(*args)
        print('*'*30)
    return inner


def plus(func):
    def inner(*args):
        print('+'*30)
        func(*args)
        print('+'*30)
    return inner

@star
@plus
def printer(msg):
    print(msg)

if __name__=="__main__":
    printer("hello")
