''' program to count number of strings from given list of strings, when
string length is two or more and first and last character is same'''

sample_list=['abc', 'xyz', 'aba', '1221','padfp']
count=0
for i in sample_list:
    if len(i)>=2 and i[0]==i[-1]:
        count+=1
print('no of such strings are:',count)
