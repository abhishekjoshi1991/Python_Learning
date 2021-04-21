import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="", database="pythondb")

# to check whether connection is took place or not

if db.is_connected():
    print('it is connected:')
else:
    print('not connected')

mycursor = db.cursor()

#lets update first row record from DB, instead of Admin and 37000 salary, update to HEAD and 80000

mycursor.execute('''DELETE FROM employee WHERE salary='80000' ''')

db.commit()

#Note**: if we omit where clause, all records get updated