'''
here we will fetch all ip's from html of webpage 'https://www.findandtrace.com/mobile-phone-number-database/Mumbai/MTNL'
'''

import re, requests
url = 'https://www.findandtrace.com/mobile-phone-number-database/Mumbai/MTNL'
r = requests.get(url)
pattern = '9\d{9}'
#127.25.99.1 or 87.256.659.25 any

matcher = re.findall(pattern, r.text)
print('total ips found=',len(matcher))
print('ips are:',matcher)