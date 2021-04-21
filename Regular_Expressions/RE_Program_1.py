# word starting with py followed by any letter from a to z three times followed by letter n

import re
matcher = re.findall('py[a-z]{3}n','this is pycoon looking for from python')
print(matcher)