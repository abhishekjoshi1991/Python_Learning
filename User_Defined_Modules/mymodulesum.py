#User Defined module

'''

whatever function we have written inside one .py file can be called into
another .py file instead of calling them in same file.

whatever packages or modules we have in python have already defined with
certain codes or prgram in it. we just import that module and make use of it
for our purpose.

similar way whatever module is defined by user must be in same path of file
in which we are calling that module or it can also be present in all modules
which are present in c drive under packages

lets define addition function (named mymodulesum)as below and lets
call it with another .py file say call.py
'''

def mysum(a,b):
    return a+b

