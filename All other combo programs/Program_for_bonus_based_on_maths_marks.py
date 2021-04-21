d1={}
roll=int(input('enter roll number:'))
d1[roll]={}
d1[roll]['name']=input('enter the students name:')
d1[roll]['marks']={}
d1[roll]['marks']['M']=int(input('maths marks:'))
d1[roll]['marks']['E']=int(input('eng marks:'))

if d1[roll]['marks']['M']>90:
    bonus=1000
elif 60<= d1[roll]['marks']['M'] <=90:
    bonus=750
else:
    bonus=500


d1[roll]['bonus']=bonus
print(d1)
