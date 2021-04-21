import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="", database= "pythondb")

#to check whether connection is took place or not

if db.is_connected():
    print('it is connected:')
else:
    print('not connected')
    
mycursor = db.cursor()
mycursor.execute('''SELECT * from employee''')

print(mycursor.fetchmany(3)) #reading first 3 records