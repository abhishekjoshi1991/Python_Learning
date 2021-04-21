#output formating or string formatting

#type 1, basic

a=90
b=10
print('sum of a and b is:',a+b) #without formating
print('sum of',a,'and',b,'is:',a+b) #with formating


#type 2, using % operator
print('\n')
print("Geeks:%2d, Portal:%5.2f" %(1, 05.333))
print("Geeks:%d, Portal:%8.5f" %(1, 05.333)) #see how space adjusted in o/p
print("Geeks:%2d, Portal:%3.1f" %(100, 05.333))



#type 3, .format() method
print('\n')
print('sum of {} and {} is '.format(a,b),a+b)
print('sum of {0} and {1} is '.format(a,b),a+b) #by refering position
print('sum of {1} and {0} is '.format(a,b),a+b)

#.format() by combining positional and keyword arguments
print('\n')
print('my name is {0} {1} {x}'.format('abhishek','ashokkumar',x='joshi'))

#.format() using numbers and positions
print('\n')
print("Geeks :{0:2d}, Portal :{1:8.2f}". format(12, 00.546)) #0-->12 and 1-->00.546
#print("Geeks :{1:2d}, Portal :{0:8.2f}". format(12, 00.546)) #this will give error that d cant used with float
print("Geeks :{a:2d}, Portal :{b:8.2f}". format(a=12, b=00.546))

#just for information, using format() in dictionary
print('\n')
tab = {'geeks': 4127, 'for': 4098, 'geek': 8637678} 

print('Geeks: {0[geeks]:d}; For: {0[for]:d}; Geeks: {0[geek]:d}'.format(tab))

#type4, f-style formatting
print('\n')
name='abhishek'
print(f'my name is {name}') #variable name value is injected into o/p

#=============================================================================================================================
#string allignment, left-center and right alligned
print('\n')
print('my name is |{}|'.format('abhijoshi'))#normal .format method
print('my name is |{:<20}|'.format('abhijoshi'))#right allign-creates 20 spaces in between ||
print('my name is |{:^20}|'.format('abhijoshi'))#center alligned
print('my name is |{:>20}|'.format('abhijoshi'))#right alligned

#=============================================================================================================================
#extra (old methods)
'''
%d – integer
%f – float
%s – string
%r - raw format
'''
string='abhi'
print('\n')
print('my name is %s' %string)
print('my name is %r' %string)#will give o/p in quotes
#print('my name is %d' %string) -->error %d format: a number is required, not str
string1=100
print('my name is %d' %string1)








