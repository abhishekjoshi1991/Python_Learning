#use of r+,w+ etc modes

#=============================================================================

#use of r+ mode (read and write)
'''
this mode just replaces characters in exisitng file during writting
it does not over writes the entire file'''

f=open(r'mode_r+_1.txt','r+')
f.write('abc')#Hel in Hello World is replaced by abc string

print(f.read())
f.close()

'''
if f.read() is called first then abc string would have written at the last
'''
f=open(r'mode_r+_2.txt','r+')
print(f.read())
f.write('abc')#Hel in Hello World is replaced by abc string
f.close()

#=============================================================================

#use of rb+ mode (read and write in binary)

f=open(r'mode_r+_3.txt','rb+')
print(f.read())
f.write('abc'.encode())#use encode function while using rb+
f.close()


#=============================================================================

#use of w mode

f=open(r'test.txt','w')
f.write('new')
f.write('new2')#is does not again overwrites the file
f.close()


#use of w+ mode (write and read mode)

f=open(r'test.txt','w+')
print(f.read())#at o/p empty string as w mode clears the file
f.write('new3')
f.close()








