#here we will create definition of decorator, then we will import this dec to
#other module named as mymodule where function definition which need to be decorated is
#written

def make_pretty(func):
    def inner():
        print('I am from inner func from decorator')
        func()
    return inner

