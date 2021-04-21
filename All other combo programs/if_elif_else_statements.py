#if,elif,else statements

'''
following is one block of code of if-elif-else and second block of code for if-else

if condition:
    print('')
elif condition2:
    print('')
else:
    print('')
if condition4:
    print('')
else:
    print('')
'''
#--------------------------------------------------------------------------------
#once one condition becomes true(if, or elif any),then python doesn't exceute other conditions
#even they are true

#example

num=10
if num<20:
    print('less than 20')
elif num<40:
    print('less than 40')

#here both conditions are true, but after first condition is true it will not
#go to elif statement, o/p only will less than 20
#--------------------------------------------------------------------------------
print('\n')
#example 2, important
    
total=100
country='US'
#country='AU'
if country=='US':
    if total <=50:
        print('shipping cost is $50')
elif total<=100:
    print('shipping cost is $25')
elif total<=150:
    print('shipping cost is $5')
else:
    print('FREE1')
if country=='AU':
    if total<=50:
        print('shipping cost is $100')
else:
    print('FREE2')

#after commenting US country, o/p will not be FREE2, because for second if block
#of code country='AU' condition satisfied, but inside condition not satisfied,
#and as if condition is satisfied it will not go to else block of free2

#check also by commenting 'AU' country
