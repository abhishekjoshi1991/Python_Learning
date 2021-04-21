#Program_to_count_and_display_vowels_in_string

string=input('enter the string:')
count=0
list1=[]
for i in string:
    if i.lower() in 'aeiou':
        count+=1
        list1.append(i)

print('no of vowels are:',count)
print('vowels present are:',list1)


#=============================================================
#with one liner or using list comprehension

print('\n')
print('using list comprehension')
vowels=[i for i in string if i.lower() in 'aeiou']
print(vowels)
print('count of vowels:',len(vowels))
