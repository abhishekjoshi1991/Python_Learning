#File Handling, use pycharm for better results

#==============================================================================
#Reading the existing file
#==============================================================================

'''first we have to open the file using open command, then we have to
read the content of the line using appropriate method

in below example we have taken 'infile' as a one object or simply one variable

to open the file in read mode use 'r' method or read method, by default file
get opened in read mode
also give file path name in raw text i.e. r''

'''
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

infile=open(r'G:\Python Ethans\All_Programs\File_Handling\F_Handling_1.txt','r')
print(infile.read())#to read complete file

'''
if we specify the parameter inside the read, e.g. infile.read(5), then it
will read only first five characters
'''

print(infile.seek(0))#to seek file to starting point

print(infile.readline())#to read only first line

''' if we have to read second or third line using readline, then we have to
use readline option two or three times'''

print(infile.seek(0))#to seek file to starting point

print(infile.readlines())#gives list of strings of each line

'''
difference between read, readline and readlines

read--> throws whole content of file in single string, and puts the cursor at end
readline--> throws one line at a time as a string
readlines --> throws whole content as a list of strings of each lines++

'''

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

'''
whatever path given above while calling the file is called as absolute path,
absolute path won't work in others system,
relative path-->it is path of file with reference to current directory,
to check the current directory use os module

w.r.t to current working directory mention the file path of file to be open
here cwd is G:\Python Ethans\All_Programs\File_Handling

we can also change the cwd using os.chdir('file path')
'''
print('\n')
import os
print(os.getcwd())
infile=open(r'.\..\pending links.txt')#(.means cwd, ..\ means one folder up)
print(infile.read())

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#==============================================================================
# Writing to a file
#==============================================================================

'''
to write a file use 'w' mode
if file is already present at particular location then it overwrites it,
by deleting the existing data, so its good practice to not the file in
write mode

if file is not present in directory, then write mode creates the new file
at that location with that file name, and start writing the data in it

after opening the file in write mode it can not be deleted unless and untill
closed, so either flush the data to hdd or close the file
'''

outfile=open(r'bbbb.txt','w')
print(outfile.write('abhishek'))
outfile.flush()#to flush the data from outfile object to hdd
#after this also we can not delete the file from hdd as it is open
outfile.close()#to close the file
'''close function also do flushing work, that is instead of flush()
if we called only outfile.close() then it would have flushed the data
to hdd also and then closes the file
'''

#==============================================================================
# Appending to a file
#==============================================================================
'''
when we need to keep content of exising file as it is, then instead of using
write mode use append mode 'a'.

append mode appends the new data to existing file
'''

infile=open(r'F_Handling_1.txt','a')
infile.write('\n new line')
infile.close()


#==============================================================================
#==============================================================================

'''
It is good practice to use the with keyword when dealing with file objects.
The advantage is that the file is properly closed, even if an exception
is raised at some point.

i.e. using with keyword we do not need to close the file again using close()
'''

with open(r'raw.txt','w') as f:
    f.write('first line')


#==============================================================================
#==============================================================================

'''
f.tell() function returns the integer value, which gives the file object's or
pointer's current position, this represented as number of bytes from the
beginning of the file 
'''

infile=open(r'F_Handling_1.txt','r')
infile.read()
print(infile.tell())

#==============================================================================
#==============================================================================

'''
we can iterate over the file,
like
infile=open(r'F_Handling_1.txt','r')
for i in infile:
    print(i)

this will print all contents from the file
'''



















