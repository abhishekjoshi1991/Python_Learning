#Object Functions for string or string methods
#e.g lower is function of str object and lower() is method
#string functions does not affects parent string

#to check available functions with objects use dir(object)
#print(dir(str))
#to get help on any function
#help(str.function_name)

#==================================================================================
#object functions and parameter taken chart

'''
+---------+-----------------------------+-------------------------------------------------+
|  Sr.No  |       Object Function       |               Parameter or Syntax               |
+---------+-----------------------------+-------------------------------------------------+
|    1	  |   capitalize	        |        takes no parameter, a.capitalize()       |
|    2	  |   lower	                |        takes no parameter, a.lower()            |
|    3	  |   upper	                |        takes no parameter, a.upper()            |
|    4	  |   count	                |        str.count(substring,start,end)           |
|    5	  |   split	                |        str.split(seperator, maxsplit=-1)        |
|    6	  |   join	                |        stringtoinsert.join(iterable of string)  |
|    7	  |   expandtabs	        |        str.expandtabs(size)                     |
|    8	  |   center	                |        str.center(size,fill_character)          | 
|    9	  |   ljust	                |        str.ljust(width,fill_character)          |
|    10	  |   rjust	                |        str.rjust(width,fill_character)          |
|    11	  |   find	                |        str.find(sub,start,end)                  |
|    12	  |   rfind	                |        str.find(sub,start,end)                  |
|    13	  |   index and rindex	        |        str.find(sub,start,end)                  |
|    14	  |   isupper and islower	|        str.isupper() and str.islower()          |
|    15	  |   startswith	        |        str.startswith(sub,start,end)            |
|    16	  |   endswith	                |        str.endswith(sub,start,end)              |
|    17	  |   strip	                |        str.strip(character)                     |
|    18	  |   lstrip and rstrip	        |        str.lstrip(character)                    |
|    19	  |   partition and rpartition	|        str.partition('seperator')               |
|    20	  |   replace	                |        str.replace('old','new',count=-1)        |
|    21	  |   title	                |        does not take any parameter              |
|    22	  |   isidentifier	        |        does not take any parameter              |
+---------+-----------------------------+-------------------------------------------------+

'''

#==================================================================================

#1. capitalize
#make the first character have upper case and the rest lower case.
abc='i am A Boy and name is Abhishek'
print(abc.capitalize())
#print(abc.capitalize) --> will throw object

#----------------------------------------------------------------------------------

#2. lower
#Return a copy of the string converted to lowercase.
#it does not change parent string
print('\n')
print(abc.lower())

#----------------------------------------------------------------------------------

#3. upper
#Return a copy of the string converted to uppercase.
#it does not change parent string
print('\n')
print(abc.upper())

#----------------------------------------------------------------------------------

#4. count
#Return the number of non-overlapping occurrences of substring
print('\n')
print(abc.count('a'))
print(abc.count('a',0,6))# searches for substring from 0 to 6 index

#----------------------------------------------------------------------------------

#5. split
# Returns a list of strings after breaking the given string by the specified separator.
#syntax: str.split(sep,maxsplit)
#default seperator(sep) is ' 'or whitespace and default maxsplit is -1
#maxsplit=maxsplit : It is a number, which tells us to split the string with provided number of times
print('\n')
print(abc.split())
print(abc.split('a'))
print(abc.split(' ',0))#no spliting occurs due to 0 even if sep is given
print(abc.split(' ',1))#splitting occurs 1 time
print(abc.split(' ',2))#splitting occurs 2 time
print(abc.split(' ',15))#splitting occurs 15 time but only 8 split happened

#if separator provided is not included in string then it returns whole
#string inside list

print(abc.split(','))

#using list comprehension to split string
string1='catbatsatfator' #split this after every 3rd letter
print([string1[i:i+3] for i in range(0,len(string1),3)])#range(start,end,increment)
#first iter:word[0:3], 2nd iter word[3:6] etc

#print file extension of file name
filename='abc.java'
print(filename.split('.')[-1])

#----------------------------------------------------------------------------------

#6. join   (opposite to split)
#concatenate any number of strings, syntax: str.join(iterables)
#iterables must contain string or list of strings or tuple of strings
#The string whose method is called is inserted in between each given string.
s1='abc'
s2='pqr'
print(s2.join(s1))# here s2 method is called (i.e join) and
#inserted between each iterables of s1

#iterables can be list of strings, opposite to o/p of split
print('#'.join(['1','2','3','4']))
print('a'.join(('1','2','3','4')))

#to join each string iterables
print(''.join(['a','b','h','i']))

#----------------------------------------------------------------------------------

#7. expandtabs
#specifies the amount of space to be substituted in string by replacing \t symbol
#default space size is 8
s='a\tb\tc'
print(s.expandtabs())#by default 8 space size is there
print(s.expandtabs(12))

#----------------------------------------------------------------------------------

#8. center
#it keeps string at center by adding fill character to left and right
#default fill character is space
#it only adds fill character when size specified is greater than len(str)
s='abcd'
print(s.center(4))#no effect
print(s.center(5))#one space to left
print(s.center(6))#one space to left and right
print(s.center(6,'#'))#add one # to left and right

#----------------------------------------------------------------------------------

#9. ljust
#returns left justified string and do padding with fill character
#default character is space

print('abhishek'.ljust(20,'-'))

#----------------------------------------------------------------------------------

#10. rjust
#returns right justified string and do padding with fill character
#default character is space

print('abhishek'.rjust(15,'-'))

#----------------------------------------------------------------------------------

#11. find
# returns lowest index position(first occurence) of substring(sub) if sub is found in string
#else returns -1

s='abhishek joshi'
print(s.find('i'))#checks and returns first index position of i
print(s.find('i',6,10))#checks for sub in 6 to 10
print(s.find('osh'))

#----------------------------------------------------------------------------------

#12. rfind
#same as find but returns highest index position(last occurence)
s='abhishek joshi'
print(s.rfind('i'))#checks and returns last index position of i

#application program
# to check given substring present in string or not
word = 'CatBatSatMatGate'
  
if (word.rfind('Ate') != -1): 
    print ("Contains given substring ") 
else: 
    print ("Doesn't contains given substring")
    
#----------------------------------------------------------------------------------

#13. index and rindex
#same as find method, but only raises an exception if value not found
#index returns lower index value and rindex returns highest index value

print(s.index('i'))
#print(s.index('g'))  --> this raises error

#----------------------------------------------------------------------------------

#14. islower
#returns True if all characters are lowercase
#o/p does not affected by numbers, spaces, symbols

print('python12$%'.islower())

#----------------------------------------------------------------------------------

#15. isupper
#returns True if all characters are lowercase
#o/p does not affected by numbers, spaces, symbols

print('Python12$%'.isupper())

#----------------------------------------------------------------------------------

#16. startswith
#returns True if string begins with specified value within given index range

print('i am a boy'.startswith('i'))
print('i am a boy'.startswith('a',2,8))
    
#----------------------------------------------------------------------------------

#17. endswith
#returns True if string ends with specified value within given index range

print('i am a boy'.endswith('i'))
print('i am a boy'.endswith(' ',2,5))#considers slicing from 2 to 5

#----------------------------------------------------------------------------------

#18. strip
#all possible leading (at start of str) and trailing (at end of str)
#characters are removed
#default character is space

print(' geeks for geeks '.strip())
print('geeks for geeks'.strip('e')) #no such character found at start or end
print('geeks for geeks'.strip('g')) #character found at start
print('geeks for geeks'.strip('gs')) #found at start and end
print('geeks for geeks'.strip('gsek')) #removes all g s e k from start and end
print('the a is the b the'.strip('the'))

#----------------------------------------------------------------------------------

#19. lstrip
#removes all leading characters
print('abhishek'.lstrip('b'))
print('abhishek'.lstrip('a'))

#----------------------------------------------------------------------------------

#20. rstrip
#removes all trailing characters
print('abhishek'.rstrip('k'))
print('abhishek'.rstrip('hk'))

#----------------------------------------------------------------------------------

#21. partition
#Partition the string into three parts using the given separator.
'''This will search for the separator in the string.  If the
separator is found,returns a tuple containing the part before the
separator, the separator itself, and the part after it.

If the separator is not found, returns a tuple containing the
original string and two empty strings.

seperator can not be empty
'''

a='abhishek @ joshi is nice @ guy'
print(a.partition('@'))
print(a.partition('#'))

#----------------------------------------------------------------------------------

#22. rpartition
'''
it splits the given string into three parts.
it start looking for separator from right side,
till the separator is found and return a tuple
which contains part of the string before separator,
seperator itself and the part after the separator.
'''
a='abhishek @ joshi is nice @guy'
print(a.rpartition('@'))
print(a.rpartition('#'))

#----------------------------------------------------------------------------------

#23. replace
#replaces all occurances of old string with new string
#syntax: replace(old,new,count=-1)
#if count not given then replaces all string otherwise
#replaces as per count given

a='abhi is good is bad is all'
print(a.replace('is','not'))
print(a.replace('is','not',1))

#----------------------------------------------------------------------------------

#24. title
#it converts string such as, words start with uppercased characters
#and all remaining cased characters have lower case.

#it converts all alphabets after digits or symbol to uppercase

print('abhishek joshi #a256b'.title())

#----------------------------------------------------------------------------------

#25. istitle
#return True if all characters are titlecased(but only first character must be uppercase)

print('Abhishek Ashok #J2D'.istitle())
print('Geeks For GEEKs'.istitle())

#----------------------------------------------------------------------------------

#26. isidentifier

#string is identifier if it contains(a-z),(A-Z),(0-9),(_) and does not
#start with number and does not contain spaces

#----------------------------------------------------------------------------------

#27. others are isalpha(),isalnum(),isdigit() etc.

