#Database Handling:
#******************

'''
concept:

why database is required:
1. to store huge data, earlier we were running the py script, data is lost once
we close the shell or file. to store the date database is required
2. to maintain data integrity
3. to maintain security

so there are multiple database platform providers, which stores our data in
encrypted format and then gives that data back to us whenever required
using proper authentication (id password). this platform providers are called
as Database Management System

to communicate with database different language is required to perform tasks
like fetching, adding, deleting data etc.

structure of database communication is generally as below:

***********            SQL(language understood by db)         **********
* Database*           <-----------------------------          *  User  *
***********             using some UI                         **********

here user communicate to db using structured query language which is
only language that db understands.

but using python, this communication will be something different.

***********            python script to communicate           **********
* Database*           <-----------------------------          *  User  *
***********             with db                               **********

but python doesn't understand SQL syntax, so python just accepts this
syntax from user and dump it to database, and vice versa

'''

#***************************************************************
#to start with database handling we need to know some SQL syntax
#***************************************************************

'''
Database Tables:
----------------
A database most often contains one or more tables. Each table is identified 
by a name. Tables contain records (rows) with data.


SQL Statements:
---------------
Most of the actions you need to perform on a database are done with SQL statements.



Keep in Mind That...
--------------------
SQL keywords are NOT case sensitive: select is the same as SELECT


Semicolon after SQL Statements?
-------------------------------
Some database systems require a semicolon at the end of each SQL statement.

Semicolon is the standard way to separate each SQL statement in database 
systems that allow more than one SQL statement to be executed in the 
same call to the server.


Some of The Most Important SQL Commands: (this commands are used with quaries)
------------------------------------------------------------------------------
 
CREATE TABLE - creates a new table (just creates structure to store data)
ALTER TABLE - modifies a table
DROP TABLE - deletes a table

INSERT INTO - inserts new data into a database
UPDATE - updates data in a database
DELETE - deletes data from a database

SELECT - extracts data from a database

CREATE DATABASE - creates a new database
ALTER DATABASE - modifies a database
CREATE INDEX - creates an index (search key)
DROP INDEX - deletes an index
'''


#*******************************************************************
# Database Handling with python using SQLITE3
#*******************************************************************

'''
there are different modules or libraries for different databases like
oracle, Mysql, Sqlite etc.
by importing these libraries we can deal or communicate with database
using python scripts.

but to deal with any database using python there are mainly 6 steps that 
need to be follow.(*imp). (here we are using sqlite3 library for practice
this sqlite3 comes with python installation.)
1. import DB library

2. create connection of py script with DB (using connect() method of sqlite3
and pass the name of the database you want to access if there is a file
with that name, it will open that file. 
Otherwise, Python will create a file with the given name.)

3. creating cursor object using connection object in step 2 to deal with DB
(Cursor is a control structure used to traverse and fetch the records of 
the database. Cursor has a major role in working with Python. 
All the commands will be executed using cursor object only.)

4. run queries with cursor object (like creating TABLE)

5. after performing these activities, commit (save) the changes, this step
is optional only used for writting the data.

6. close the connection object
'''