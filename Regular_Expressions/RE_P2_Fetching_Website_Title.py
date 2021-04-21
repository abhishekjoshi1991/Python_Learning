#Printing title of websites like flipkart, amazon etc. for this we need
#to use title tag of html to fetch the title, <title> </title>

import re, requests
sites = ['https://www.flipkart.com/','https://www.amazon.in/']
print('o/p without grouping')
for each in sites:
    r = requests.get(each)
    pattern = '<title>.*</title>' #we need any characters(.) * occurences
    matcher = re.finditer(pattern, r.text)
    for i in matcher:
        print('Title of this website is:', i.group())

'''
if we program like this then it will fetch the title with title tags also, we just need
text inside those tags.
now this is obvious that we have to use <title> as part of pattern, but if when we
need only certain text from o/p, then we group that parameter from where that text is coming
using () braces inside definition of pattern

so instead of '<title>.*</title>' expression we will use '<title>(.*)</title>'

so while printing the result we need to pass i.group(1) as we have created first group,
be default i.group() takes 0 as an argument inside braces
'''
print('\n')
print('\o/p with grouping')
for each in sites:
    r = requests.get(each)
    pattern = '<title>(.*)</title>' #we need any characters(.) * occurences
    matcher = re.finditer(pattern, r.text)
    for i in matcher:
        print('Title of this website is:', i.group(1))