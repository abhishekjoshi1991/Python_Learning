#Modules
#------------------------------------------------------------------------------
'''
module is nothing but .py file in which different functions are
defined.(contains Python definitions and statements.)

those functions can be imported from module as per the requirement

For example: math module contains different functions like
factorial, sin, cos etc. these functions can be imported
individually or we can import whole package itself.

But when we import whole package we have to use
modulename.functionname() to perform the operation

means

if we import math module whole then we can't use directly
factorial(5), we have to use math.factorial(5)
'''
import math
#print(factorial(5)),error factorial is not defined
print(math.factorial(5))



'''
there is another way to import factorial from math

like this if we only import specific function from module then
we can use factorial(5) directly
'''
from math import factorial
print(factorial(6))



'''
instead of importing single single functions from a module,
we can use 'from module import *' to use functions directly
without using module name before as in case 1 above

* import all functions and we can use them directly

* imports all the names from a module to current namespace
'''
from math import *
print(factorial(7))
print(sqrt(900))



'''
module can be imported as a shortcut name also, so as
to reduce effort of typing the module name
'''
import math as m
print(m.sqrt(400))


'''
multiple functions can also be imported at a time from module
e.g: from math import factorial, sqrt, log
'''

#---------------------------------------------------------------
'''
difference between
import math and import math as * is well explained in video
modules and user defined modules from 14:00 mintutes
'''
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

#Some modules
print('\n')
print('os module')
import os
print(os.getcwd())
os.mkdir('Folder')#two make new directory or folder in cwd
#os.chdir(to change cwd)
os.rmdir('Folder')#to remove the directory

#os.walk module
'''
syntax: os.walk('path of directory')
output:
('',[],[])-->tuple of string, list1 and list2
string-->path of directory
first list-->list of folder in that directory
second list--> list of files in that directory

in this way it can return multiple tuples if directory contains multiple
folder and files

os.walk gives generator object, so we need to iterate over it
'''
for i in os.walk('G:\Python Ethans\Lecture Recodings'):
    print(i)

'''
o/p of above program as follow
('lect recording folder path',[folder1, folder 2 name],[all files in lect recording]),
('folder 1 path',[folders in folder1],[files in folder 1]),
('path of abc folder in folder 1',[folder in abc if any],[files in abc if any]),
('path of folder 2',[folder in folder 2],[files in folder 2])

in this way will get 4 tuples
'''
#let say we want to print all mp4 files from lecture recording folder
'''
('',[list1],[list2])
we have iterate over os.walk by 3 iterator x,y,z where
print(x) will gives all folder path in strings
print(y) will gives all list1
print(z) will give all list 2
'''
for x,y,z in os.walk('G:\Python Ethans\Lecture Recodings'):
    for each in z:#as we are interested in last list as it contains files
        if each.split('.')[-1]=='mp4':
            print(each)
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------            
            

print('\n')
print('random module')
import random
print(random.randint(0,5))#to print random int from 0 to 5
print(random.random())#to print float between 0 to 1
print(random.random()*100)#to print float between 0 to 100
print(random.choice([1,2,3]))#to choose random element from iterable
l1=[1,23,4,5,6,5]
print(random.shuffle(l1))#to shuffle the list not tuple

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------


print('\n')
print('calendar module')
import calendar
print(calendar.month(2020,12))#to print calendar of given month
print(calendar.calendar(2018))#to print whole calendar of sp. year

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

print('\n')
print('pickle module')
'''
pickle module dumps the python object into some file in binary format and
then we can unpack it whenever required

in standard word it implements binary protocols for serializing and
de-serializing python object.

pickle module is risky because of risk of unpacking of file from unknown resource
suntax:
to dump the object--> pickle.dump(objecttodump,file)

'''
import pickle
l1=[1,2,3,4,'abhi']
fileobj=open('G:\Python Ethans\All_Programs\pickle.txt','wb')#use rb and wb mode always
pickle.dump(l1,fileobj)#file wil be returned in encrypted format
fileobj.close()

#to retrive file again to console
infile=open('G:\Python Ethans\All_Programs\pickle.txt','rb')
print(pickle.load(infile))


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------











