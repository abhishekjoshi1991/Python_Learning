import sqlite3
try:
    with sqlite3.connect('Employee') as db: #no need to use db.close() then in finally
        mycursor = db.cursor()
        mycursor.execute('''SELECT * FROM emp''') #to fetch all data
        #print(mycursor.fetchone()) #to fetch first record, cursor will go at end of first record
        #print(mycursor.fetchall()) #to fetch all data, cursor will go at last
        #print(mycursor.fetchmany(2)) #will fetch first two record, here empty as cursor is at last, try using this code one at a time

        #we can also iterate on cursor like infile object
        for each in mycursor:
            print(each)

except Exception as E:
    print('unable to interact with DB:',E)

else:
    print('data fetched successfully!')
    db.commit()
    db.close()

