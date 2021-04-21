import sqlite3
try:
    db = sqlite3.connect('Employee')
    mycursor = db.cursor()
    mycursor.execute('''DELETE FROM emp WHERE empID='1' ''') #to add single row at a time

except Exception as E:
    print('unable to interact with DB:',E)

else:
    print('worked fine!')
    db.commit()

finally:
    db.close()