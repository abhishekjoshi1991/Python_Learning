#Program to count number of uppercase and lowercase characters

#=======================================================================================
str1=input('enter the string:')

#using buit-in functions
lower,upper=0,0
for i in str1:
    if i.islower():
        lower+=1
    elif i.isupper():#can't assign directly else here, otherwise will count spaces
        upper+=1
    else:
        pass

print('No of lower case characters:',lower)
print('No of upper case characters:',upper)

#=======================================================================================
#using ord() function
#ord('a')=97, ord('z')=122
#ord('A')=65, ord('Z')=90

print('\n')
l,u=0,0
for i in str1:
    if 97<= ord(i) <=122:
        l+=1
    elif 65<= ord(i) <=90:
        u+=1
    else:
        pass

print('lower case characters:',l)
print('upper case characters:',u)

#=======================================================================================

print('\n')
l1,u1=0,0
for i in str1:
    if 'a'<= i <='z':
        l1+=1
    elif 'A'<= i <='Z':
        u1+=1
    else:
        pass
print('lower case characters:',l1)
print('upper case characters:',u1)
