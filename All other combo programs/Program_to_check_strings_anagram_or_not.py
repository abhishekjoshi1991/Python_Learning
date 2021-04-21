#program to check strings are Anagram or not
#each character from first string present in other string

#listen and silent are anagram


s1=input('enter first string:')
s2=input('enter second string:')
if sorted(s1)==sorted(s2):
    print('two strings are anagram to each other')
else:
    print('strings are not anagram')



#using function

def ana(s1,s2):
    if sorted(s1.lower())==sorted(s2.lower()):
        return 'are anagram'
    else:
        return 'not anagrams'

print(ana('silent','Listen'))
