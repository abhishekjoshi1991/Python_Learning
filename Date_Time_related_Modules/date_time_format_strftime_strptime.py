#date and time formatting in python:
#**********************************

'''
The way date and time is represented may be different in different places, organizations etc.
It's more common to use mm/dd/yyyy in the US, whereas dd/mm/yyyy is more common in the UK.

Python has strftime() and strptime() methods to handle this.

The strftime() method is defined under modules date, datetime and time whereas
strptime() method is datetime class method

                        strftime                        strptime
Usage           Convert object to a string
                according to a given format            Parse a string into a datetime object
                                                        given a corresponding format

Type of method  Instance method                         Class method
Method of       datetime; time                          datetime
Syntax          strftime(format)                        strptime(date_string, format)

so objects created from date, datetime, and time all support a strftime(format) method, 
and it creates the string as per the given format.


Format Codes for strftime and strptime:
#*************************************

%a :                Abbreviated weekday name.                                               Sun, Mon
%A :                Full weekday name.                                                      Sunday, Monday,
%w :                Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.       0, 1, …, 6
%d :                Day of the month as a zero-padded decimal.                              01, 02, ..., 31
%b :                Abbreviated month name.                                                 Jan, Feb, ..., Dec
%B :                Full month name.                                                        January, February,
%m :                Month as a zero-padded decimal number.                                  01, 02, ..., 12
%y :                Year without century as a zero-padded decimal number                    00,01,02----,99
%Y :                Year with century as a decimal number.                                  0001, 0002, …, 2013, 2014,--9999
%H :                Hour (24-hour clock) as a zero-padded decimal number.	                00, 01, ..., 23
%I	:               Hour (12-hour clock) as a zero-padded decimal number.	                01, 02, ..., 12
%p	:               Locale’s AM or PM.	                                                    AM, PM
%M	:               Minute as a zero-padded decimal number.	                                00, 01, ..., 59
%S	:               Second as a zero-padded decimal number.	                                00, 01, ..., 59
%j	:               Day of the year as a zero-padded decimal number.	                    001, 002, ..., 366
%U	:               Week number of the year (Sunday as the first day of the week).          00, 01, ..., 53
%W	:               Week number of the year (Monday as the first day of the week).          00, 01, ..., 53
%c	:               Locale’s appropriate date and time representation.	                    Mon Sep 30 07:06:05 2013
%x	:               Locale’s appropriate date representation.	                            09/30/13
%X	:               Locale’s appropriate time representation.	                            07:06:05
'''

import datetime
import time


#A. strftime():
#**************

'''
used to convert datetime obj to string.
let's format the current time as per the format below
'''
my_time=datetime.datetime.now()
print(my_time)
f1=my_time.strftime("%H:%M:%S") #here : is seperator, we can specify any
#or we can use as below, datetime.strftime(datetime_obj,format)
print(datetime.datetime.strftime(my_time,"%H:%M:%S"))
print('formatted time:',f1)
f2=my_time.strftime("%d-%m-%y")
print('formatted date:',f2)
f3=my_time.strftime("%d/%m/%Y, %H:%M:%S")
print(f3)
print(type(f3))

#formatting using timestamp obtained date
print('\n')
print('formatting using timestamp obtained date')
timestamp = 1528797322
date_time = datetime.datetime.fromtimestamp(timestamp)
print("Date time object:", date_time)
d = date_time.strftime("%m/%d/%Y, %H:%M:%S")
print("Output:", d)

#Locale’s appropriate date and time representation.
print('\n')
print('Locale’s appropriate date and time representation')
print(my_time.strftime("%c"))
print(my_time.strftime("%x"))
print(my_time.strftime("%X"))



#B. strptime():
#**************
'''
exactly opposite as that of strftime, converts datetime string to
datetime object.

arguments required:
1. string representing date and time
2. string formatting code equivalent to string (means in whatever format
string is mentioned is same format, format code must be wriiten)
'''
print('\n\n')
print('strptime')
my_string = "10/12/2020 04:19:56"
#here date is seperated by / and time by :
new_time_obj_created = datetime.datetime.strptime(my_string,"%d/%m/%Y %H:%M:%S") #format specified as per input string
print(new_time_obj_created)
print(type(new_time_obj_created))

date_string = "21 June, 2018"
date_object = datetime.datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)
print("type of date_object =", type(date_object))