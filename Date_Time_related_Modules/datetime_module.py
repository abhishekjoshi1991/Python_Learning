# Datetime_Module:
#*****************

'''
A module named datetime can be imported to work with the date
as well as time.Datetime module comes built into Python, so there
is no need to install it externally.

Datetime module supplies classes to work with date and time.

These classes provide a number of functions to deal with dates,
times and time intervals

commonly used classes in datetime module are:

datetime Class
time Class
date Class
timedelta Class

we can check other classes using, dir(datetime)
'''

'''
epoch time:(or Unix time or POSIX time or Unix timestamp)
epoch: it is taken at January 1st at midnight 00:00:00 and
Unix: it is taken at January 1st 1970 at midnight 00:00:00

from this time, number of seconds passed until we can calculate
in time module

'''

#******************
#A. datetime class
#******************


import datetime
#or from datetime import datetime


#To Get Current Date and Time

'''
one of the class defined in datetime module is datetime.
we then use now() method to create object of that datetime

we can also today() method which will give same o/p.
'''

print(datetime.datetime.now()) #Returns new datetime object representing current local time
print(datetime.datetime.today())
datetime_obj=datetime.datetime.now() #saved object into variable

#from current time data (above data) we can extract following

print(datetime_obj.date()) #to print date without time
print('month:',datetime_obj.month)
print('day:',datetime_obj.day)
print('year:',datetime_obj.year)
print('current time:',datetime_obj.time()) #to print time without date
print('cuurent hour:',datetime_obj.hour)
print('current mins:',datetime_obj.minute)
print('current seconds:',datetime_obj.second)
print('current microseconds:',datetime_obj.microsecond)



'''
we can also construct our own datetime using datetime constructor
in the format as

datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]

while constructing own datetime, year, month and day are mandatory fields
other are optional.

MINYEAR(1) <= year <= MAXYEAR(9999)
1 <= month <= 12
1 <= day <= number of days in the given month and year
0 <= hour < 24
0 <= minute < 60
0 <= second < 60
0 <= microsecond < 1000000

let's construct our own datetime
'''
print('\n')
print('constructing own time')
new_date=datetime.datetime(2020,12,31) # or (2020,12,31,13,56,26,658)
print(new_date.year)
print(new_date.month)
print(new_date.day)



#**************
# B. time class
#**************

'''
we can use time class to create time object. time() act as constructor

syntax:  datetime.time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None,)
0 <= hour < 24
0 <= minute < 60
0 <= second < 60
0 <= microsecond < 1000000

this method returns an object.

all arguments are optional.tzinfo may be None. The remaining arguments may be ints

we can import time class as 
from datetime import time or simply we can import datetime
'''
print('\n\n')
print('time class')
print(datetime.time()) #with no arguments passed
print(datetime.time(minute=12)) #with only single argument passed
print(datetime.time(23,56,25)) # with three arguments passed
new_time=datetime.time(23,56,25) #saved obj to variable

#now we can call all methods with this object, like
print(new_time.hour)

#**************
# C. date class
#**************

'''
we can use date class to create date object. date() act as constructor

syntax:  datetime.date(year, month, day)
MINYEAR <= year <= MAXYEAR
1 <= month <= 12
1 <= day <= number of days in the given month and year

this method returns an object.

Constructor of this class needs three mandatory arguments year, month and date

we can import date class as 
from datetime import date or simply we can import datetime
'''
print('\n\n')
print('date class')
my_date = datetime.date(1996, 12, 11)
#all functions can be calles using this object as,
print(my_date.today()) #will print today's date
print(my_date.day)

'''we can also calculate date from timestamp, using number of seconds passed
between epoch time and particular date. for this we can use fromtimestamp()
if method:
'''
time_stamp=datetime.date.fromtimestamp(1326244364)
print('timestamp date:',time_stamp)


#*******************
# D. timedelta class
#*******************

'''
this class is generally used to calculate difference between dates,
also used in date manipulations

syntax:
datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, 
minutes=0, hours=0, weeks=0)
'''
print('\n\n')
print('timedelta class')
from datetime import timedelta
initial_date=datetime.datetime.now()
final_date=initial_date + timedelta(days=365) #date after 365 days
print('future date:',final_date)

#to calculate differnce between dates
t1=timedelta(days=2,hours=1)
t2=timedelta(days=4,hours=2)
print(t2-t1)

#-ve timedelta objects
t3=timedelta(seconds=50)
t4=timedelta(seconds=55)
print(t3-t4)

