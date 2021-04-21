#Regular Expressions: RegEx:
#***************************

'''
Regular Expression, is a sequence of characters that forms a search pattern.
RegEx can be used to check if a string contains the specified pattern we want to search

import in built re module for RegEx.


Function in RegEx
#################
match : try to apply the pattern at start of string only and returns match object,
        it returns none if no match found
        syntax: re.match(pattern, string, flags=0)
search :scan through string to search for pattern, returns match object
        based on first occurance of pattern only, even if multiple patterns
        are found, return none if no pattern found
        syntax: re.search(pattern, string, flags=0)
findall:Returns a list containing all matches
        syntax: re.findall(pattern, string, flags=0)
split:  The split() function returns a list where the string has been split
        at each match
        If the pattern is not found, re.split() returns a list containing the original string
sub :   the sub() function replaces the matches with the text of your choice:
        If the pattern is not found, re.sub() returns the original string
subn:   it returns a tuple of 2 items containing the new string and the number of substitutions made.
finditer: throws iterator object of all matched patterns in which all matched objects would be there


#methods associated with match object
group() : method returns the part of the string where there is a match.
         by default group() takes 0 as an argument inside braces,
         if specific group number is specified then it will print that
         group only
start() : function returns the index of the start of the matched substring
end()   : returns the end index of the matched substring.
string  :  attribute returns the passed string.
re      : attribute of a matched object returns a regular expression object(i.e. pattern)

let's go through example below
'''

import re
print('o/p of match function')
print('*'*25)
matcher = re.match('python','python is easy python language')
print(matcher) #it found match at start from index 0 to 6(excluding)

#changing case of python letter in string
matcher = re.match('python','Python is easy python language')
print(matcher)  #returns None, as no pattern found at start of string

#ignoring cases using ignorecase flags
matcher = re.match('python','python is easy python language',re.I) #or re.IGNORECASE
print(matcher) #now found the match with case ignored

'''as seen o/p of above programs, it is clear that 
match searches for pattern at start only and it throws match object, 
with index span and match found
we can print the start and end index, and found match as below'''
print('functions associated with match object')
print(matcher.start())
print(matcher.end())
print(matcher.group())

#let take another e.g to see functions associated with match object
r = re.search('(\d{3}) (\d{2})','39801 356, 2102 1111')
#to find three digit number followed by space followed by two digit number
#two combinations are there using findall [('801', '35'), ('102', '11')]
#here we created two group (\d{3}) and second is (\d{2})
print(r)
print(r.group())#available only with search not with findall
print(r.group(1)) #will print text from first group only
print(r.group(2)) #will print text from second group only
print(r.start())
print(r.end())
print(r.string)
print(r.re)
#***************************************************************************************
print('\n')
print('o/p of search function')
print('*'*25)
matcher = re.search('python','Python is easy python language of python lovers')
print(matcher)
'''
as seen from above, re.search() function searches for first occurence of pattern,
here due to Uppercase P character it has skipped first python word and printed
first occurence in index span (15,21)
'''

#***************************************************************************************
print('\n')
print('o/p of findall function')
print('*'*25)
matcher = re.findall('python','Python is easy python language of python lovers')
print(matcher)
'''
as seen from above, re.findall() function searches for all occurences of pattern,
and returns list of all matched patterns, if no pattern found then returns empty list
'''

#***************************************************************************************
print('\n')
print('o/p of split function')
print('*'*25)
matcher = re.split('\s','the rain in spain')
print(matcher) #split at whitespace
matcher = re.split('r','the rain in spain')
print(matcher) #split at r
#we can control the number of occurrences by specifying the maxsplit parameter:
matcher = re.split('\s','the rain in spain',maxsplit=1)
print(matcher) #split at max 1 whitespace

#***************************************************************************************
print('\n')
print('o/p of sub function')
print('*'*25)
matcher = re.sub('\s','#','the rain in spain')
print(matcher) #replaces whitespaces by #
#we can control the number of replacements by specifying the count parameter:
matcher = re.sub('\s','#','the python is an easy language',count=2)
print(matcher)

#***************************************************************************************
print('\n')
print('o/p of subn function')
print('*'*25)
matcher = re.subn('\s','','the rain in spain')
print(matcher) #remove all whitespaces, 3 replacement made

#***************************************************************************************
print('\n')
print('o/p of finditer function')
print('*'*25)
p = re.finditer('py[0-9]{2}n','py89n is py66n of words')
print(p) #will throw iterator object
for all in p:
    print(all.start(),all.end(), all.group())


#***************************************************************************************
#***************************************************************************************
'''
In RegEx metacharacters are used in patterns

Different metacharacters are:
'''
#***************************************************************************************
print('\n')
print('*******************************')
print('Metacharacters in RegEx')
print('*******************************')
#1. []
'''
it represents set of characters,
example - [a-m]
Characters can be listed individually, e.g. [amk] will match 'a' or 'm', or 'k'

Ranges of characters can be indicated by giving two characters and separating them by a '-', for example [a-z]
[0-5][0-9] will match all the two-digits numbers from 00 to 59

If - is escaped (e.g. [a\-z]) or if it’s placed as the first or last character (e.g. [-a] or [a-]), it will match a literal '-' also

[^0-9] means will match any character including space other than 0 to 9

Expression	        String	        Matched?
[abc]	            a	            1 match
                    ac	            2 matches
                    Hey Jude	    No match
                    abc de ca	    5 matches
'''
#Find all lower case characters alphabetically between "a" and "m"

print('1. o\p from metacharacter []')
r = re.findall('[a-m]','The rain in Spain')
print(r)

#find all lower case character only 'a','e','n'
r = re.findall('[aen]','The rain in Spain')
print(r)
r = re.findall('[aen]','pytho ot goad')
print(r)

#find two digit number from string say 78
r = re.findall('[0-9][0-9]','The rain in 78 Spain')
print(r)

r = re.findall('[a\-m]','The rain in - Spain')
print(r)

r = re.findall('[^0-9]','this is 9 part')
print(r)

#removing punctuation from string
test = 'this is a string! But it has punctuation. How to remove?'
clean = re.findall(r'[^!.? ]+',test) #all ! ? . and space is removed
print(' '.join(clean)) # to join all string together with space

#grabing only hypenated words from string say abhi-joshi
test1 = 'only find the hypen-word from sentence do not know how-long'
p1 = re.findall(r'[\w]+-[\w]+',test1)
print(p1)


#***************************************************************************************

#2. dot(.) or period
'''
In the default mode, this matches any character except a newline. 
If the DOTALL flag has been specified as re.DOTALL, this matches any character including a newline.

Expression	    String	    Matched?
..	            a	        No match
                ac	        1 match
                acd	        1 match
'''
print('\n')
print('2. o\p from metacharacter .dot')
r = re.findall('ra.n','The rain in Spain ra$n ra\nn')
print(r) #searches for any character as replacement for .dot
r = re.findall('ra..n','The raipn in Spain ra$n ra\nn')
print(r)
#with DOTALL flagprint('\n')
r = re.findall('ra.n','The rain in Spain ra$n ra\nn',re.DOTALL)
print(r)

#***************************************************************************************

#3. ^(caret)
'''
matches the start of string, means is pattern is present at start of string or not

Expression	    String	    Matched?
^a	            a	        1 match
                abc	        1 match
                bac	        No match
'''
print('\n')
print('3. o\p from metacharacter ^')
r = re.findall('^hello','Hello i am saying hello')
print(r) #no match
r = re.findall('^hello','hello i am saying hello')
print(r)

#***************************************************************************************

#4. $
'''
Check if the string ends with pattern passed, 

Expression	    String	    Matched?
a$	            a	        1 match
                formula	    1 match
                cab	        No match
'''
print('\n')
print('4. o\p from metacharacter $')
r = re.findall('world$','this is last statement of world')
print(r)

#***************************************************************************************

#5. *
'''
causes zero or more occurences of preceding letter of pattern, means 
ab* will match zero or more occurences of preceding character (b) and
hence result may be a, ab or a followed by no of occurences of b

Expression	String	    Matched?
ma*n	    mn	        1 match
            man	        1 match
            maaan	    1 match
            main	    No match (a is not followed by n)
            woman	    1 match
'''
print('\n')
print('5. o\p from metacharacter *')
r = re.findall('ab*', 'i am abhishek abbbsh')
print(r)
'''here 'am' has zero occurence of b, 'abhishek' has 1
occurence of b and 'abbbsh' has 3 occurences of b'''


#***************************************************************************************

#6. +
'''
Causes the resulting RE to match 1 or more repetitions of the preceding RE.
ab+ will match ‘a’ followed by any non-zero number of ‘b’s

Expression	String	    Matched?
    ma+n	mn	        No match (no a character)
            man	        1 match
            maaan	    1 match
            main	    No match (a is not followed by n)
            woman	    1 match
'''
print('\n')
print('6. o\p from metacharacter +')
r = re.findall('aix+', 'The rain in Spain falls mainly in the plain!')
print(r)
'''here there no such letter in string, where 'ai' is 
followed by 'x', hence o/p is blank list
'''


#***************************************************************************************

#7. {}
'''
exactly matches specified number of occurences mentioned in {}.
fewer matches cause the entire RE not to match.
For example, a{6} will match exactly six 'a' characters, but not five.

Note**: ab{2} will match two occurence of b and not ab, always 
consider immediate preceding character

{m,n} Causes the resulting RE to match from m to n repetitions of the preceding RE,
attempting to match as many repetitions as possible. For example, a{3,5} will match from 3 to 5 'a' characters. 
Omitting m specifies a lower bound of zero, and omitting n specifies an infinite upper bound.

As an example, a{4,}b will match 'aaaab' or a thousand 'a' characters followed by a 'b', but not 'aaab'

{m,n}? causes the resulting RE to match from m to n repetitions of the preceding RE, 
attempting to match as few repetitions as possible
For example, on the 6-character string 'aaaaaa', a{3,5} will match 5 'a' characters, while a{3,5}? 
will only match 3 characters.
'''
print('\n')
print('7. o\p from metacharacter {}')
r = re.findall('al{2}','The already in Spain falls mainly in the plain')
print(r) #matches exactly two occurence of 'l' after 'a'
r = re.findall('abhi{1,3}','my name is abhiiiishek and abhi')
print(r) #will match max 3 characters in abhiiiishek
r = re.findall('abhi{1,3}?','my name is abhiiiishek and abhi')
print(r) #will match least character
r = re.findall('[0-9]{2,4}','my name is 12 and 345673')
print(r) #see o/p carefully

#***************************************************************************************

#8. ?
'''
The question mark symbol ? matches zero or one occurrence of the pattern left to it.
Expression	        String	            Matched?
ma?n	            mn	                1 match
                    man	                1 match
                    maaan	            No match (more than one a character)
                    main	            No match (a is not followed by n)
                    woman	            1 match
'''
print('\n')
print('8. o\p from metacharacter ?')
r = re.findall('ma?n','find in mn and man in maaaan')
print(r)


#***************************************************************************************

#9. |
''' Vertical bar | is used for alternation (or operator)
the target string is scanned, REs separated by '|' are tried from left to right.

Expression	    String	    Matched?
a|b	            cde	        No match
                ade	        1 match (match at ade)
                acdbea	    3 matches
'''
print('\n')
print('9. o\p from metacharacter |')
x = re.findall("falls|stays", 'The rain  in Spain falls mainly in the stays plain')
print(x)

#***************************************************************************************

#10. () group
'''
Parentheses () is used to group sub-patterns. For example, (a|b|c)xz match any string that matches 
either a or b or c followed by xz

Expression	    String  	Matched?
(a|b|c)xz	    ab xz	    No match
                abxz	    1 match (match at abxz)
                axz cabxz   2 matches
'''
print('\n')
print('10. o\p from metacharacter ()')
x = re.findall('(a|b?y)p','this is bypass factor in refrigeration')
print(x)


#***************************************************************************************

#11. \ (backslash)
'''
Either escapes special characters (permitting us to match characters like '*', '?', and so forth), or 
signals a special sequence described below section

for e.g. \$a match if a string contains $ followed by a. Here, $ is not interpreted by a RegEx engine 
in a special way that is as metacharacter.

lets escape special character disccused above  and see the output
'''
print('\n')
print('11. o\p from metacharacter "\"')
r = re.findall('ma*n', 'it is man document')
print(r)
r = re.findall('m\a*n', 'it is mn man document')
print(r) #it has escaped special meaning of \a*, printed mn only

#***************************************************************************************
#***************************************************************************************

#********************
# Special sequences :
#********************

'''
Special sequences make commonly used patterns easier to write. Here's a list of special sequences:
'''
print('\n')
print('*****************************')
print('Special Characters in RegEx')
print('*****************************')

#1. \A - Matches if the specified characters are at the start of a string
print('\n')
print('1. o\p from special character \A')
r = re.findall('\Athe','the sun is throwing heat')
print(r)
r = re.findall('\Ahe','the sun is throwing heat')
print(r)

#2. \b - Matches if the specified characters are at the beginning or end of a word.
'''
Expression	    String	        Matched?
\bfoo	        football	    Match
                a football	    Match
                afootball	    No match
foo\b	        the foo	        Match
                the afoo test	Match
                the afootest	No match
'''
print('\n')
print('2. o\p from special character \b')
r = re.search('\bain','the rain in spain')
print(r) #Check if "ain" is present at the beginning of a WORD:
r = re.findall(r'ain\b','the rain in spain') #without raw text ans differs
print(r) #Check if "ain" is present at the end of a WORD:

#3. \B - Opposite of \b. Matches if the specified characters are present but not at the beginning or end of a word.
'''
Expression	        String	        Matched?
\Bfoo	            football	    No match
                    a football	    No match
                    afootball	    Match
foo\B	            the foo	        No match
                    the afoo test	No match
                    the afootest	Match
'''
print('\n')
print('3. o\p from special character \B')
r = re.search(r'\Bent','the entomology is pentos study')
print(r)
r = re.search(r'ent\B','development is intercontinental') #without raw text ans differs
print(r)


#4. \d - Matches any decimal digit. Equivalent to [0-9]
'''
Expression	String	    Matched?
\d	        12abc3	    3 matches (at 12  3)
            Python	    No match
'''
print('\n')
print('4. o\p from special character \d')
r = re.search('\d','he is 28 years old')
print(r) #only one match at 2, as we are using search function
r = re.findall('\d','he is 28 years old')
print(r)
#to match group of digit together, we can use \d+
r = re.findall('\d+','his birthdate is 30 april 1991')
print(r)
#if d+ not used o/p will be like 3,0,1,9,9,1

#5. \D -  Matches any non-decimal digit. Equivalent to [^0-9]
print('\n')
print('5. o\p from special character \D')
r = re.findall('\D','he is 28 years old')
print(r)


#6. \s - Matches where a string contains any whitespace character.
print('\n')
print('6. o\p from special character \s')
r = re.findall('\s','this is Python language')
print(r)
r = re.search('\sP','this is Python language')
print(r)


#7. \S - Matches where a string contains any non-whitespace character.
print('\n')
print('7. o\p from special character \S')
r = re.findall('\S','this is Python language')
print(r)
r = re.search('\Sth','this is Python language')
print(r) #any non white space character followed by th


#8. \w : Matches any alphanumeric character (digits and alphabets).
# this is Equivalent to [a-zA-Z0-9_],  underscore _ is also considered an
# alphanumeric character. it does not include whitespace character
print('\n')
print('8. o\p from special character \w')
r = re.findall('\w','this is _ Python language')
print(r)
#to match the group of character we use \w+
r =re.findall('\w+','his birthdate is 30 april 1991')
print(r)


#9. \W: Matches any non-alphanumeric character. Equivalent to [^a-zA-Z0-9_]
print('\n')
print('9. o\p from special character \W')
r = re.findall('\W','this is _ @ Python language')
print(r)

#10. \Z: Matches if the specified characters are at the end of a string.
print('\n')
print('10. o\p from special character \Z')
r = re.search('Python\Z','this Python language of Python')
print(r)



'''
Sets
A set is a set of characters inside a pair of square brackets [] with a special meaning:

Set	        Description	
[arn]	    Returns a match where one of the specified characters (a, r, or n) are present	
[a-n]	    Returns a match for any lower case character, alphabetically between a and n	
[^arn]	    Returns a match for any character EXCEPT a, r, and n	
[0123]	    Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
[0-9]	    Returns a match for any digit between 0 and 9	
[0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
[a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case	
[+]	        In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for 
            any + character in the string
'''


#compile function with RegEx
'''
instead of syntax like, r= re.search(pattern, string) we can use following using compile method

a=re.compile(pattern)
a.search(string)
'''
print('\n')
print('compile function')
x = re.compile('\d')
matcher = x.search('i a 568 string')
print(matcher)
