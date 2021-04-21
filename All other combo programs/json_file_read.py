#Reading and writing json file from/to local:
#*******************************************

'''
json: JavaScript Object Notation

json is file format in which data is stored in stuctured manner
just like dictionary interms of key: value pair

difference between json and python dict

python                  json
-------                 ------
dict object             json object
list,tuple              array
int,float               number
str                     string
True                    true
False                   false
None                    null
'''


#1. Reading from a Json file using json.load:
#*******************************************

'''
to read json file, we need to import json library first

read the source file and create file object using regular
file handling concept.

use json.load to read content of the file
'''
print('reading from json file')
import json
infile = open(r'sample_json.json') #created infile's object
data = json.load(infile)
print(data)
print(type(data))

'''
from o/p it is clear that, some keywords from json file are automatically
converted to python keywords, like null __> None
true __> True etc.
'''


#2. Writing code to json file format using json.dump:
#****************************************************

'''
lets read data from sample_json file and using this data we 
will create backup of json file as backup_sample_json

to dump the date to json file, use json.dump command

syntax: json.dump(dictionary, file pointer)
where, dictionary – name of dictionary which should be converted to JSON object.
file pointer – pointer of the file opened in write or append mode.
'''

print('\n')
print('writing to a json file:')
infile = open(r'sample_json.json') #created infile's object
data = json.load(infile)
outfile= open(r'backup_sample_json','w')
json.dump(data,outfile)
outfile.close()

'''
here, again python keywords are converted to json keywords
'''


#3. Reading from a web using json.loads():
#********************************************

'''
when we have content of json in string format then we can use
json.loads(). here s in loads stand for string
'{"name":"abhi","salary":20000}'
'json inside string'

for json.load() it require infile object or file object but 
for json.loads() it requires string object to pass inside

lets read content from website 'https://api.github.com/'
using request library and then will use json.loads() on it
'''

print('\n')
print('reading from web and applying json.loads()')

import requests
r=requests.get(r'https://api.github.com/') #using requests.get() HTML of web page is fetched
#here html page is nothing but json format
print(r) #to get response code
'''
response codes:
200: for success
400: Bad Request
403: Forbidden
404: Not Found
'''
print(r.text) #to print the data from web
print(type(r.text)) # retrieving data in string format, where inside string json is there
data = json.loads(r.text) #applying this loads() on string JSON
print(data)
print(type(data))
#as it is dictionary, we can fetch keys and values
print(data.keys())

'''
so json.loads() either takes following:
1. json.loads(josn_string)  or 
2. json.loads(fileobject.read()) provided that file has json structure
'''



#4. writing dictionary to file using json.dumps():
#************************************************

'''
json.dumps() creates json object and convert dictionary into
json string, this json string then can be written to file using
write method of file handling

syntax: json.dumps(dictionary_object)
'''

print('\n')
print('writing dictionary to file using json.dumps()')
dictionary={
    "name" : "sathiyajith",
    "rollno" : 56,
    "cgpa" : 8.6,
    "phonenumber" : "9976770500"
}
json_object=json.dumps(dictionary)
print(type(json_object)) #type will be string
#so we can write this string to file
with open(r'backup_sample_json_dumps','w') as outfile:
    outfile.write(json_object)



