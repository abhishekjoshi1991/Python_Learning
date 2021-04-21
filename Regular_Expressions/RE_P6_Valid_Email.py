import re

'''
valid email id is:
1. 1 to 20 lowercase, uppercase and numbers plus ._%+-
2. an @ symbol
3. 2 to 20 lowercase, uppercase, numbers plus .-
4. A period (i.e dot)
5. 2 to 3 lowercase and uppercase letters
'''

str = 'sk@aol.com  md@.com  @seo.com  dc@.com  abhi@gmail.com'

r =re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}",str)

print(r)