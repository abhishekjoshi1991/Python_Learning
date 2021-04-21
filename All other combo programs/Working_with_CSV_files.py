#Working with csv files
#-----------------------------------------------------------------
'''
it is comma separated values which store tabular data.
each line of csv file is data records.
each csv file may contains one or more field(header row)

to work with csv file, import csv module first

if we read csv file directly using file handling concepts then o/p will
be in plain text format. so their are different functions asscociated
with csv modules

functions of csv modules..
1. reader()--> it throws the result in list format, where each list
represents each row
syntax: csv.reader(fileobject)

2.DictReader-->it throws o/p is dictionary format where,
header row data considered as keys and record data(other than header
row is considered as a values)

both reader and DictReader throws object, so we need to iterate over it
'''

import csv
infile=open('G:\Python Ethans\All_Programs\csvexcelfile.csv')
for i in infile:
	print(i)

print('\n')
infile=open('G:\Python Ethans\All_Programs\csvexcelfile.csv')	
for i in csv.reader(infile):
	print(i)

print('\n')
infile=open('G:\Python Ethans\All_Programs\csvexcelfile.csv')	
for i in csv.DictReader(infile):
	print(i)
#or
print('\n')
infile=open('G:\Python Ethans\All_Programs\csvexcelfile.csv')
for i in csv.DictReader(infile):
	print(dict(i))

#-----------------------------------------------------------------
#-----------------------------------------------------------------	
'''
difference between reader and DictReader--
----------------------------------------

suppose csv file contains thousand of column where one column is
for salary of emp, then it is impossible to fetch that only
column using reader function as it requires that column number.

while DictReader provides structured o/p hence salary can be
fetched directly using salary as a key

let's fetch salary of mp for above csv using both functions
'''
print('\n')
print('differene between reader and DictReader')
#using reader
infile=open('G:\Python Ethans\All_Programs\csvexcelfile.csv')
for i in csv.reader(infile):
	print(i[2])#as salary in 3rd column fetch 2nd index of list
#csv.reader will print header row also in o/p

	
#using DictReader
print('\n')
infile=open('G:\Python Ethans\All_Programs\csvexcelfile.csv')
for i in csv.DictReader(infile):
	print(i['Salary'])#so from key name, data is fetched


'''
to print each row data one by one we can use next function by
calling it multiple times, to print header row use
next function only once and to print other data we can iterate over
it afterwards as

.next() method returns the current row and advances the iterator
(cursor)to the next row
.
'''
print('\n')
infile=open('G:\Python Ethans\All_Programs\csvexcelfile.csv')
a=csv.reader(infile)
print(next(a))

'''
Note:
csv file with tab as a delimiter can be read as,
csv.reader(infile,delimiter='\t')

to know more about various parameters in csv.reader() visit
https://www.programiz.com/python-programming/reading-csv-files
'''

#-----------------------------------------------------------------
#-----------------------------------------------------------------	

#Writing to CSV file:
#--------------------

#csv.writer()
'''
to write to a CSV file in Python, we can use the csv.writer() function.

the csv.writer() function returns a writer object that converts the
user's data into a delimited string. This string can later be used
to write into CSV files using the writerow() function

csv.writerow() writes one row at a time and csv.writerows() function writes
multiple row at a time
'''
import csv
with open('G:\Python Ethans\All_Programs\createdcsv.csv','w') as outfile:
        obj=csv.writer(outfile)
        obj.writerow(["SN", "Movie", "Protagonist"])
        obj.writerow([1, "Lord of the Rings", "Frodo Baggins"])
        obj.writerow([2, "Harry Potter", "Harry Potter"])    

#writing multiple rows with writerows
mult=[["SN", "Movie", "Protagonist"], [1, "Lord of the Rings", "Frodo Baggins"],
               [2, "Harry Potter", "Harry Potter"]]
with open('G:\Python Ethans\All_Programs\createdcsv.csv','a') as outfile:
        obj=csv.writer(outfile)
        obj.writerows(mult)


#csv.DictWriter()
'''
csv file can be written from python dictionary using DictWriter function
syntax:csv.DictWriter(file, fieldnames)

fieldnames:a list (object) which should contain the column headers specifying
the order in which data should be written in the CSV file
'''
import csv
mydict =[{'branch': 'COE', 'cgpa': '9.0', 'name': 'Nikhil', 'year': '2'}, 
         {'branch': 'IT', 'cgpa': '9.3', 'name': 'Aditya', 'year': '2'}, 
         {'branch': 'SE', 'cgpa': '9.5', 'name': 'Sagar', 'year': '1'}]
fields=['branch','cgpa','name','year']
with open ('G:\Python Ethans\All_Programs\createdcsv.csv','a') as outfile:
        obj=csv.DictWriter(outfile,fieldnames=fields)
        obj.writeheader()
        obj.writerows(mydict)







