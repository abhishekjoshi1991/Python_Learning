#Program to check string is palindrom or not
#e.g. nitin is palindrom as it is same in both directions
#but Nitin is not palindrom, case sensitive

string=input('enter the string:')
if string==string[::-1]:
    print('string is palindrom')
else:
    print('string is not palindrom')


print('\n')
#using reversed keyword

if string==''.join(reversed(string)):
    print('string is palindrom')
else:
    print('string is not palindrom')
