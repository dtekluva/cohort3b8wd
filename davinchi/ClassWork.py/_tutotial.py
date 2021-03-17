#!/usr/bin/python3

import pymysql

# Open database connection
db = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='testdb',
                             cursorclass=pymysql.cursors.DictCursor)

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
# cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
# data = cursor.fetchone()
# print ("Database version : %s " % data)

# disconnect from server
# db.close()

for i in range(12):

# Prepare SQL query to INSERT a record into the database.
    sqol = """INSERT INTO EMPLOYEE(FirstName,
            LastName, Age, Sex, Income)
            VALUES ('Mac', 'Mohan', 21, 'M', 12000)"""

    sqel = """INSERT INTO EMPLOYEE(FirstName,
            LastName, Age, Sex, Income)
            VALUES ('Johnson', 'Mobolaji', 24, 'M', 32000)"""

    sql = """INSERT INTO EMPLOYEE(FirstName,
            LastName, Age, Sex, Income)
            VALUES ('Ayisa', 'Yetunde', 22, 'F', 10000)""" 
    try:
         # Execute the SQL command
        cursor.execute(sqol)
        cursor.execute(sqel)
        cursor.execute(sql)
        # print("There")
             # Commit your changes in the database
        db.commit()
    except SyntaxError:
        # Rollback in case there is any error
        # print("here")
        db.rollback()
 