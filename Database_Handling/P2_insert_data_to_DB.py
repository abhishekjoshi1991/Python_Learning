import sqlite3
try:
    db = sqlite3.connect('Employee')
    mycursor = db.cursor()
    data = ((2,'abhishek','IT',25000),(3,'sukanya','PHP',35000), (4,'harsh','surabhi',50000))
    mycursor.execute('''INSERT INTO emp VALUES (1,'mach','HR',45000)''') #to add single row at a time

    mycursor.executemany('''INSERT INTO emp VALUES (?,?,?,?)''',data) #to add multiple data at a time, takes two arguments


except Exception as E:
    print('unable to interact with DB:',E)

else:
    print('worked fine!')
    db.commit()

finally:
    db.close()