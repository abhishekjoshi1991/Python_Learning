#String Updation and Deletion
'''
In Python, Updation or deletion of characters from a String is not allowed.
This will cause an error because item assignment or item deletion from a
String is not supported. Although deletion of entire String is possible
with the use of a built-in del keyword. This is because Strings are immutable,
hence elements of a String cannot be changed once it has been assigned.
Only new strings can be reassigned to the same name.
'''

#updating single character
s='abhishek'
#s[1]='P' -->error str object does not support item assignment

#deletion of single character
#del s[2] -->'str' object doesn't support item deletion

#deleting entire string
del s
#print(s) --> no string to print in database now
