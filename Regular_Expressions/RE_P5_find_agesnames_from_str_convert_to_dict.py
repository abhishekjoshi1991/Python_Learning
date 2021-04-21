import re

string = 'Janice is 23 and Theon is 35 while Gabriel is 44 and Mark is 50'

#Pattern for name is Letter start with Upper case and other are lowercase

patname = '[A-Z][a-z]*'
patage = '\d{1,2}'

names = re.findall(patname,string)
ages = re.findall(patage,string)

dict = {}
x = 0

for each in names:
    dict[each] = int(ages[x])
    x = x+1

print(dict)