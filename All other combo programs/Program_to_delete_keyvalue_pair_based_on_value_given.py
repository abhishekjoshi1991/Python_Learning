#Program to remove key value pair for user defined value


d1={1:1,2:4,3:9,4:16,5:9,6:9,7:49}
num=int(input('enter number to remove:'))
for each in d1:
    if d1[each]==num:
        del(d1[each])
print(d1)
'''this program will throw an error of dict changed size during iteration,
because at a same time we are iterating on dict and deleting items from it also,
to avoid these we can create copy of dict to iterate over it as below'''

        

print(d1)
d1={1:1,2:4,3:9,4:16,5:9,6:9,7:49}
d2=d1.copy()
num=int(input('enter number to remove:'))
for each in d2:
    if d1[each]==num:
        del(d1[each])

print(d1)
