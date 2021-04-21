'''
large data can be handled using executemany() function that already seen.

also multiple queries can be passed using executescript() function for sqlite3 not for mysql
This is a convenience method for executing multiple SQL statements at once.
It executes the SQL script it gets as a parameter.
'''

import sqlite3

db = sqlite3.connect('Emp')
mycursor = db.cursor()


mycursor.executescript(""" 
    CREATE TABLE people( 
        firstname, 
        lastname, 
        age 
    ); 
   
    CREATE TABLE book( 
        title, 
        author, 
        published 
    ); 
   
    INSERT INTO 
    book(title, author, published) 
    VALUES ( 
        'Dan Clarke''s GFG Detective Agency', 
        'Sean Simpsons', 
        1987 
    ); 
    
    INSERT INTO 
    people(firstname, lastname, age) 
    VALUES ( 
        'abhishek', 
        'joshi', 
        30 
    );
    
    INSERT INTO 
    people(firstname, lastname, age) 
    VALUES ( 
        'sukanya', 
        'joshi', 
        27
    ); 
    """)

sql = """ SELECT * FROM book;"""
sql2 = """ SELECT * FROM people;"""
mycursor.execute(sql)
result = mycursor.fetchall()
print(result)
print('\n')
mycursor.execute(sql2)
result1 = mycursor.fetchall()
print(result1)
