# Creating first DB using sqlite3, with blank table:
#***************************************************

import sqlite3 #step 1
try:
    db = sqlite3.connect('Employee') #step 2, connection object named db
    mycursor = db.cursor() #step3, cursor object named mycursor
    mycursor.execute('''CREATE TABLE if not exists emp
    (empID int NOT NULL,
    empName varchar(80),
    dept text,
    salary int,
    PRIMARY KEY (empID))''') #step 4, use SQL query using cursor object

except Exception as E:
    print('unable to interact with db:',E)

else:
    print('Table created successfully!')

finally:
    db.close() #step 6, closing connection


'''
this will create a new database file with name Employee in the directory
which is in encrypted format.

in step 2, using connect method of sqlite3, we have created connection with
DB named as Employee, and it have created connection object db.

in step 3, using that connection object named db, we have cursor method to 
create cursor object named mycursor

in step 4, using execute method of cursor object, we fired query to create a table
name emp

here strp 5 not mentioned as we are not writing anything to DB

in step 6, using connection object named db, we have closed the connection with DB.


once Employee DB file is generated and again if we try to run the program, it will
throw an error that table is already exists. thus we need to use query 
'CREATE TABLE if not exists emp' instead of just 'CREATE TABLE emp' query


also here we are using sqlite3 for practice only, in reality db.connect('Employee')
will not work unless and untill given with proper authentication.
'''