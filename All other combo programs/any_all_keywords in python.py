#'any' and 'all' keywords in python

#any
'''
returns true if all items are true
returns false if all are false or iterables is empty
similar to or operator
syntax: any(list of iterables)
'''

print('output of any keywords')
print(any([False,True,False,False]))
print(any([False,False,False]))
print('\n')

#========================================================

#all
'''
return true if all items are true or iterable is empty
syntax: all(list of iterables)
'''

print('output of all keywords')
print(all([False,True,False,False]))
print(all([True,True,True]))
