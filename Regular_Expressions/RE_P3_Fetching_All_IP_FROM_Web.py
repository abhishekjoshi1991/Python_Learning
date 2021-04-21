'''
here we will fetch all ip's from html of webpage 'https://get-site-ip.com/'
'''

import re, requests
url = 'https://get-site-ip.com/'
r = requests.get(url)
pattern = '[0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}'
#127.25.99.1 or 87.256.659.25 any

matcher = re.findall(pattern, r.text)
print('total ips found=',len(matcher))
print('ips are:',matcher)