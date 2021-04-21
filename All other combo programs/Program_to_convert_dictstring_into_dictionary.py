#Program to convert string as a dict into dictionary
'''
i/p-->'1:prashant,2:sandeep,3:aakash'
o/p-->{1:'prashant',2:'sandeep',3:'aakash'}

split string two times, first with ',' and then ':'
'''

inp='1:prashant,2:sandeep,3:aakash'
print(dict([[y for y in x.split(':')]for x in inp.split(',')]))
#this will keep intgers 1,2,3 in strings only
#to convert them into integers also use following

print({int(x.split(':')[0]):(x.split(':')[1]) for x in inp.split(',')})


