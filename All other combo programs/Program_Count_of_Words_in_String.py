#count of words in string
#'i am a boy' has 4 words

string='i am a boy'
#Solution-1: count number of spaces and count+1 gives no of words

count=0
for i in string:
    if i==' ':
        count+=1
else:
    print('no of words:', count+1)

#=====================================================================

#solution-2: using split method
print('number of words:',len(string.split()))


#=====================================================================

#solution-3: using count method
print('no of words:',string.count(' ')+1)
