#Exception Handling:
#--------------------

'''
Exceptions are raised when the program is syntax wise correct but the code
resulted in an error. This error does not stop the execution of the program,
however, it changes the normal flow of the program.

exception can be handled by using following syntax:

try:
       # Some Code to check.... 

except:
       # optional block
       # Handling of exception (if required)

else:
       # execute if no exception

finally:
      # Some code .....(always executed even if exception occurs)

'''
#-------------------------------------------------------------------------------
#let's consider the program which gives rise the error or exception
a=100
#print(a/0)


'''
in above, exception will raise as divison by zero,
when we don't know in which line exception is going to raise or whenever
we are suspecting some line of code that may be get fail, we put that line
of code in try block.

within the try block, if program sees any possible exception then control goes
to except block of code, and whatever code inside except block is executed.

let's try above example with try and except block
'''


#use of try and except
#=====================
print('use of try and except')
try:
    a=100
    print(a/0)
except:
    print('possible divison by zero is occur')

'''
in above case, we have put possible error code inside try block, when try
block sees an exception is coming out it throws control to except block

that means it says , if exception is occur, excute except block of code, thus
print statement will get exceuted

thus we can say, this exception handling code does not throw red error as occur
usually
'''

#-------------------------------------------------------------------------------
'''
if we know, what will be the exact error, then we can write that error name
infront of except block also, means'''
print('\n')
print('except block with exact error name specified')
try:
    a=100
    print(a/0)
except ZeroDivisionError:
    print('possible divison by zero is occur')

#but remember if we spell error name incorrectly or put other error name infront
#of except block then error will be their in o/p
#that means we can't use as follows

'''
try:
    a=100
    print(a/0)
except IndexError:
    print('possible divison by zero is occur')

so it will show ZeroDivisionError
'''

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

#use of try and multiple except
#==============================

'''
we can have more than one except block, but only one except block is executed
as per the program.

'''
print('\n')
print('multiple except block')
try:
    a=3
    if a<4:
        b=a/(a-3)
except IndexError:
    print('incorrect index')
except ZeroDivisionError:
    print('again zero in denominator')


'''
so in above example, division by zero error is sure, so only second except block
is exceuted, and not except block that contains indexerror msg

so as per the program, control decided to which except block it must go

we can also write above code as,(that means multiple except inside  ())

try:
    a=3
    if a<4:
        b=a/(a-3)
except (IndexError,ZeroDivisionError):
    print('error is coming')

'''

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

#use of try, except and else
#==============================
'''
else block can be present after all except blocks. The code enters the else block
only if the try clause does not raise an exception.
'''
print('\n')
print('try,except,else block')
def func(a,b): 
    try: 
        c = ((a+b) / (a-b)) 
    except ZeroDivisionError: 
        print("a/b result in 0")
    else: 
        print(c)

func(2,3)
func(3,3)

#*Note: either except or else get exceuted at a time
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

#use of try, except,else and finally
#===================================

'''
finally block of code is always excuted even if exception is raised or not
in try block
'''

print('\n')
print('try,except,else and finally block')
def func(a,b): 
    try: 
        c = ((a+b) / (a-b)) 
    except ZeroDivisionError: 
        print("a/b result in 0")
    else: 
        print(c)
    finally:
        print('i get printed always')
func(2,3)
func(3,3)   

#*Note: we have only two scenario, (try,except,finally) or (try,else,finally)
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

#to print exception name(generic exception: "except Exception as E")
#=======================
print('\n')
print('try,except,else and finally block')
def func(a,b): 
    try: 
        c = ((a+b) / (a-b)) 
    except Exception as E: #this is generic (global)class for all exception
        print(E)


func(3,3)   


#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

#Need of finally block
#=======================

'''
if we check follwing program P1, then we will come to know that even if we are not
using finally block then also last print statement gets executed, then why we
need finally block
'''
#P1: without finally block
print('\n')
print('without finally block')
 
try: 
    a=10/0
    print(a)
except Exception as E: 
    print(E)  
print('finally')


'''
in above last print statement gets executed even we have not used finally


Let's have another scenario, where we are getting the exception inside the
except block which handles exception, in such case our last print statement won't
get executed as below P,

print('\n')
print('without finally block and exception in except')
try: 
    a=10/0
    print(a)
except Exception as E: 
    print(E)
    import abcde
print('finally')


so in such case we need finally, so finally ensure that even if
there is error in except block or at other, always execute finally P3
so program will surely throw an error but finally block get executed



print('\n')
print('with finally block and exception in except')
try: 
    a=10/0
    print(a)
except Exception as E: 
    print(E)
    import abcde
finally:
    print('finally done')


'''

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

#where to generic and other exception(which one get excuted)
#============================================================
#here we have defined generic exception at last, so control will go to
#generic exception only if exception won't get covered in first two except block
#that means it has found exception which is not covered in first two

print('\n')
print('where to use generic')
try:
    num=int(input('enter number:'))
    l1=[1,2,3,4]
    print(3/num)
    print(l1[3])
    import abcd
except ZeroDivisionError as E:
    print(E)
    print('Line1')
except IndexError as E:
    print(E)
    print('Line2')
except Exception as E:
    print('Generic exception is being printed')
else:
    print('no exception')
finally:
    print('finally done')

'''
run above code with:
1. num=0--> control goes two first exception and will print Line1
2. make l1[5] and num>0-->control will directly go to IndexError except block  and will
print Line 2
3. put import abcd inside try block, num>0 and l1[3]--> import error won't be
handled by first two exception, hence control directly will go to generic
exception
'''

#------------------------------------------------------------------------------
'''
now question will be, whatif we put generic exception at start and then other
specific exception after it
'''
try:
    num=int(input('enter number:'))
    l1=[1,2,3,4]
    print(3/num)
    print(l1[3])
    import abcd
except Exception as E:
    print('Generic exception is being printed')
except ZeroDivisionError as E:
    print(E)
    print('Line1')
except IndexError as E:
    print(E)
    print('Line2')

else:
    print('no exception')
finally:
    print('finally done')
    
'''
in such case, it will always execute generic exception, no matter what exception
is


*Note:so always specify specific exception block first and then generic exception
'''

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

#Multiple exception in Try block:(but only one generic exception)
#================================================================
print('\n')
print('multiple exception in try block')
try:
    l1=[1,2,3,4]
    print(l1[6])
    print('this statement will not execute')
    import abcd
except Exception as E:
    print(E)
else:
    print('no exception')
finally:
    print('finally done')

'''
in above, we will get only one exception msg as E, for index error, thus even
if we have multiple exception then after first exception is hit rest program
is not executed, thus print statement is try block not printed in o/p
'''



#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

#Raising an exception
#====================
'''
raise statement allows the programmer to raise a specific exception
if certain condition does not occur
'''

print('\n')
print('raising an exception')
try:
    num=int(input('enter the number:'))
    if num<2:
        raise ValueError('Pls Enter num greater than 2!!')
    print(100/num)
except ValueError as V:
    print(V)
else:
    print('No exception')
finally:
    print('THE END')

'''
run above program with num=1 and then num>2

instead of ValueError we can not use other name like AbhiError'''





#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

#saving Program context
#======================

'''
sometimes data we have entered in fields get lost if some exception
occurs, like in IRCTC website,

so to save data till exception is raised is called as saving program
context

let, we want to print numbers from 1 to 10, and when num==7 then we
have to raise exception explicitly, then continue with next numbers
'''


print('\n')
print('saving program context')
try:
    for i in range(1,11):
        if i==7:
            raise
        print(i)#till here nums from 1 to 6 get printed
except Exception as E:#it will come here when num=7
    print(E)#will raise the exception
    for j in range(i+1,11):
        print(j)#to continue to print num from 8 to 10
else:
    print('No exception')
finally:
    print('THE END')




#if we are not using else block then its ok, then sequence will be
#try,except,finally-- but if we are using else block then sequence
#can not be try,except,finally,else it has to be try,except,else,finally










