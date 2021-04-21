#Leap Year
'''
Year which is divisible by 100 but not divisible by 400 is not leap year (this
is specially for century year)
and
year which is divisible by 4 or 400 (after first condition is false) is leap year
'''

#===================================================================
#Program 1

year=int(input('enter the year:'))
if year%100==0 and year%400!=0:
    print('Year is not Leap year')
elif year%4==0 or year%400==0:
    print('Year is leap year')


#===================================================================

#Program 2
print('\n')
year=int(input('Enter the year:'))
if year%4==0:
    if year%100==0 and year%400!=0:
        print('year is Not Leap year')
    else:
        print('year is leap year')
