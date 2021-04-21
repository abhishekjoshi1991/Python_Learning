#Program on file handling

#1.Creating backup of a file
'''
let's create backup of F_Handling_1 file
'''

infile=open(r'F_Handling_1.txt','r')
outfile=open(r'F_Handling_1_Backup.txt','w')
outfile.write(infile.read())#can't pass infile inside write, write takes str
outfile.close()


#2. Creating backup of image
'''
let's create backup of 1.jpeg image
'''

infile=open(r'G:\Python Ethans\All_Programs\File_Handling\1.jpg','rb')
outfile=open(r'G:\Python Ethans\All_Programs\File_Handling\1back.jpeg','wb')
outfile.write(infile.read())
outfile.close()

'''
so while reading the image file, read the image using 'rb' read binary format
also while writting it us 'wb' format i.e. write binary
'''

#3.we can also use rb mode to read text file
infile=open(r'F_Handling_1.txt','rb')
r=infile.read()
print(r[0])#so it stores data in binary format
print(ord('T'))
print(r)#b is attached before string

#4.use of seek and read function

infile=open(r'F_Handling_1.txt','r')
print(infile.read())

'''to seek to 6th byte or to start from 6th byte in file'''
print(infile.seek(5))
print(infile.read())#see now printing taking place from is leaving first 5 char

'''to read first 10 characters'''
infile.seek(0)
print(infile.read(10))
