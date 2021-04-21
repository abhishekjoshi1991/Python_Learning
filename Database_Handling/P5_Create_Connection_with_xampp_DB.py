'''
we can connect to database created using mysql under xampp, using mysql.connector library

we have already created pythondb database in which we have created employee table
in that we does not have set the auto increment parameter, so we need to pass ID field
'''

import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="", database= "pythondb")

#to check whether connected or not, use code below
if (db): #or if db.is_connected():
    print('successful')
else:
    print('not success')


mycursor = db.cursor()
mycursor.execute('''INSERT INTO employee VALUES (1,'joshi','ADMIN',37000)''')

data = ((2,'abhishek','IT',25000), (3,'sukanya','PHP',35000), (4,'harsh','surabhi',50000))
mycursor.executemany('''INSERT INTO employee (id,name,department,salary) VALUES  (%s,%s,%s,%s)''',data) #we need same structure using placeholders

db.commit()
db.close()