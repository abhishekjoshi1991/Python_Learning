#Conditional statement assignment

'''
Program 1
WAP to take a string from user and if it is a list then print last element
of the list otherwise print message 'It is not a list'
'''

string=input('enter the string as a list as [1,2,3]:')
if type(eval(string))==list:
    print(eval(string)[-1])
else:
    print('it is not a list')
