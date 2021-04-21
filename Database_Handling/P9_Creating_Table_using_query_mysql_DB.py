import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="") #here we haven't passed database name, as we need to create it first

# to check whether connection is took place or not

if db.is_connected():
    print('it is connected:')
else:
    print('not connected')


mycursor = db.cursor()
mycursor.execute('''CREATE DATABASE student''')
db.close()

db = mysql.connector.connect(host="localhost", user="root", password="",database="student") #we need to create connection again
mycursor = db.cursor()
#create table under student
mycursor.execute('''CREATE TABLE if not exists details
    (empID int NOT NULL,
    empName varchar(80),
    dept text,
    salary int,
    PRIMARY KEY (empID))''')


