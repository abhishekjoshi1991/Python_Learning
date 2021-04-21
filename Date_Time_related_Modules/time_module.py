# Time Module in Python:
#***********************

'''
This module provides various functions to manipulate time values.

we need to import time module first to use all the functions.
'''

import time

#commonly used functions/methods are:

#1. time.time()
'''
this returns number of seconds passed since epoch (Unix 1st jan 1970, midnight)
'''
print('\n')
print('o/p of time.time()')
print('seconds since epoch:', time.time())


#2. time.ctime()
'''
this function  takes seconds passed since epoch as an argument and 
returns string representing local time.

syntax: time.ctime(no of seconds from epoch)
'''
print('\n')
print('o/p of time.ctime()')
print('ctime:', time.ctime(1611739432.0002277))

#3. time.sleep()
'''
The sleep() function suspends (delays) execution of the current thread for the given number of seconds.
syntax: time.sleep(no of sec to sleep)
'''
print('\n')
print('o/p of time.sleep()')
print('hello')
time.sleep(2)
print('world')


'''
struct_time class in python: 

Several functions in the time module such as gmtime(), asctime() etc. either 
take time.struct_time object as an argument or return it.
(it is time value as returned by gmtime(), localtime(), and strptime() and 
accepted as an argument by asctime(), mktime() and strftime())

it may be considered as a sequence of 9 integers.

time.struct_time(tm_year=2018, tm_mon=12, tm_mday=27, 
                    tm_hour=6, tm_min=35, tm_sec=17, 
                    tm_wday=3, tm_yday=361, tm_isdst=0)
                    
tm_isdst is daylight saving time.

Index	Attribute	Values
0	    tm_year	    0000, ...., 2018, ..., 9999
1	    tm_mon	    1, 2, ..., 12
2	    tm_mday	    1, 2, ..., 31
3	    tm_hour	    0, 1, ..., 23
4	    tm_min	    0, 1, ..., 59
5	    tm_sec	    0, 1, ..., 61
6	    tm_wday	    0, 1, ..., 6; Monday is 0
7	    tm_yday	    1, 2, ..., 366
8	    tm_isdst	0, 1 or -1
'''


#4. time.localtime()
'''
the localtime() function takes the number of seconds passed since epoch as an
argument and returns struct_time in local time.
'''
print('\n')
print('o/p of time.localtime()')
result = time.localtime(1611739432.0002277)
print("localtime:", result)
print("year:", result.tm_year)
print("tm_hour:", result.tm_hour)


#5. time.gmtime()
'''
The gmtime() function takes the number of seconds passed since epoch as an argument and returns struct_time in UTC.

UTC is coordinated universal time, indian time (IST) is 5 hours and 30 minutes ahead of Coordinated Universal Time.
'''

print('\n')
print('o/p of time.gmtime()')
result = time.gmtime(1611739432.0002277)
print("gmtime:", result)
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)


#6. time.mktime()
'''
The mktime() function takes struct_time as an argument (or a tuple containing 9 elements corresponding
to struct_time) and returns the seconds passed since epoch in local time. 
Basically, it's the inverse function of localtime().
'''

print('\n')
print('o/p of time.mktime()')
result = time.mktime((2021,1,27, 9, 23, 52, 2, 27,0))
print("mktime:", result)


#7. time.asctime()
'''
The asctime() function takes struct_time (or a tuple containing 9 
elements corresponding to struct_time) as an argument and returns a string representing it.
'''
print('\n')
print('o/p of time.asctime()')
result = time.asctime((2021,1,27, 9, 23, 52, 2, 27,0))
print('asctime:',result)



#8. time.strftime()
'''
The strftime() function takes struct_time (or tuple corresponding to it) as an
argument and returns a string representing it based on the format code used
'''
print('\n')
print('o/p of time.strftime()')
local_time = time.localtime(1611739432.0002277)
new = time.strftime("%m/%d/%Y, %H:%M:%S",local_time)
print(new)


#9.time.strptime()

'''
The strptime() function parses a string representing time and returns struct_time

#i don't know but already seen strptime is with datetime module only 
'''
print('\n')
print('o/p of time.strptime()')
time_string = "21 June, 2018"
result = time.strptime(time_string, "%d %B, %Y")
print(result)